from .utils import save_to_csv
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .extractor import extract_pdf, extract_img
from .utils import save_to_csv
import os

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_path = os.path.join('media', uploaded_file.name)

            # Save the uploaded file
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # Depending on the file type, call the appropriate extraction function
            if file_path.endswith('.pdf'):
                extracted_text = extract_pdf(file_path)
            elif file_path.endswith(('.png', '.jpg', '.jpeg')):
                extracted_text = extract_img(file_path)
            else:
                return render(request, 'pdf_app/error.html', {'error': 'Invalid file format. Please upload a JPEG, PNG or PDF file.'})

            # Save the extracted text to a CSV file
            csv_file_path = os.path.join('media', 'extracted_data.csv')
            save_to_csv(extracted_text, csv_file_path)

            # Pass the extracted text to the template
            return render(request, 'pdf_app/display_text.html', {'text': extracted_text})

    else:
        form = UploadFileForm()

    return render(request, 'pdf_app/upload.html', {'form': form})












