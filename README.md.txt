#Resume-Builder
Resume Builder is a Django-based web application designed to generate both single and bulk resumes using pre-defined formats. It eliminates the manual effort required to create resumes in MS Word and introduces automation by uploading Excel data to generate multiple resumes at once.
<br>

###🚀 Features
📄 Generate Single Resume – Enter details manually and choose from 3 default templates.

📥 Bulk Resume Generation – Upload an Excel file with candidate data and generate resumes instantly.

🗃️ Data Management – Store and retrieve user data from a database.

🖨️ Export – Export resumes in structured format.

<br>
###🛠️ Installation
run git clone https://github.com/Naren-18/Resume-Builder.git

run cd Resume-Builder

run pip install -r requirements.txt

run python manage.py migrate

run python manage.py createsuperuser

<br>
###🚀 Run the Project
run python manage.py runserver

Open http://127.0.0.1:8000/ in your browser

<br>
###🖼️ Screenshots
Add your screenshots to a screenshots/ folder and reference them like this:

![Single Resume Form](./screenshots/single-resume-form.png)

![Bulk Upload](./screenshots/bulk-upload.png)

![Generated Resume](./screenshots/generated-resume.png)

<br>
###📦 Tech Stack
Python

Django

HTML/CSS/Bootstrap

SQLite / PostgreSQL

<br>
###🏗️ System Overview
Existing System:

Manual resume creation using MS Word.

No central database.

Can only create one resume at a time.

Drawbacks:

Time-consuming.

No data reusability.

Cannot generate resumes in bulk.

Proposed System:

Single resume generation as in the existing system.

Bulk generation from Excel file upload.

Database integration for data storage.

Supports mass generation of resumes in seconds.

<br>
###📚 Django Modules Used
Models – Define structure for personal, educational, and skill details.

Views – Handle HTTP requests and render templates.

Templates – Control layout of generated resumes.

URL Routing – Maps user requests to appropriate views.

<br>
###👥 Contributors
Narendra Kumar