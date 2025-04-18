import boto3
import uuid
from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
db = SQLAlchemy()

# Limit the file types that can be uploaded to S3.
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class File(db.Model):
    # All SQLAlchemy models need an ID.
    id = db.Column(db.Integer, primary_key=True)
    original_filename = db.Column(db.String(100))

    # Changed filename
    filename = db.Column(db.String(100))
    bucket = db.Column(db.String(100))
    region = db.Column(db.String(100))

def create_app():
    load_dotenv()
    app = Flask(__name__)

    # Configures the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    db.init_app(app)

    # Routes
    @app.route("/", methods=["GET", "POST"])
    def index():

        # Checks if the user is trying to POST
        if request.method == "POST":
            uploaded_file = request.files["file-to-save"]
            if not allowed_file(uploaded_file.filename):
                return "File not allowed"

            # New file names are generated uniquely using UUID. Appends original file extension.
            new_filename = uuid.uuid4().hex + '.' + uploaded_file.filename.rsplit('.',1)[1].lower()

            # Create the S3 variable that lets us interact with S3.
            bucket_name = os.getenv("AWS_BUCKET_NAME")
            region = os.getenv("AWS_REGION")

            s3 = boto3.resource(
                "s3",
                region_name=region,
                aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
            )

            s3.Bucket(bucket_name).upload_fileobj(uploaded_file, new_filename)

            # Save a reference to the cloud file in our local database.
            file = File(original_filename=uploaded_file.filename, filename=new_filename,
                        bucket=bucket_name, region=region)
            db.session.add(file)
            db.session.commit()

            return redirect(url_for("index"))

        # Does this if user is trying to GET
        files = File.query.all()

        return render_template("index.html", files=files)
    return app