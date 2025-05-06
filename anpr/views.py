import cv2
import easyocr
import os
from django.shortcuts import render, redirect
from .forms import VideoUploadForm
from .models import UploadedVideo
from django.conf import settings
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage
from PIL import Image as PILImage


def extract_text_from_video(video_path, output_folder):
    reader = easyocr.Reader(['en'])
    detected_data = []

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 30 == 0:
            frame_filename = f"frame_{frame_count}.jpg"
            frame_path = os.path.join(output_folder, frame_filename)
            cv2.imwrite(frame_path, frame)

            detected_text = reader.readtext(frame_path, detail=0)
            text = " ".join(detected_text) if detected_text else "No text detected"

            detected_data.append({
                'frame': frame_filename,
                'path': frame_path,
                'text': text
            })

    cap.release()
    return detected_data


def create_excel_report(detected_data, output_excel_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Detected Plates"
    ws.append(['Frame Image', 'Detected Text'])

    for index, data in enumerate(detected_data, start=2):
        # Insert image
        img = PILImage.open(data['path'])
        img.thumbnail((150, 150))
        temp_thumb = data['path'].replace('.jpg', '_thumb.jpg')
        img.save(temp_thumb)

        excel_img = ExcelImage(temp_thumb)
        img_cell = f'A{index}'
        ws.add_image(excel_img, img_cell)

        # Insert text
        ws[f'B{index}'] = data['text']

    wb.save(output_excel_path)


def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video_instance = form.save()

            video_path = video_instance.video.path
            media_folder = os.path.join(settings.MEDIA_ROOT, f'video_{video_instance.id}')
            os.makedirs(media_folder, exist_ok=True)

            detected_data = extract_text_from_video(video_path, media_folder)

            excel_path = os.path.join(media_folder, 'detected_output.xlsx')
            create_excel_report(detected_data, excel_path)

            video_instance.detected_text = "\n".join([d['text'] for d in detected_data])
            video_instance.output_excel = f'video_{video_instance.id}/detected_output.xlsx'
            video_instance.save()

            return redirect('video_result', video_id=video_instance.id)
    else:
        form = VideoUploadForm()

    return render(request, 'anpr/upload_video.html', {'form': form})


def video_result(request, video_id):
    video_instance = UploadedVideo.objects.get(id=video_id)
    return render(request, 'anpr/video_result.html', {'video': video_instance})
