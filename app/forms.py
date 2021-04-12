from flask_wtf import FlaskForm
from wtforms import TextAreaField, FileField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description = TextAreaField("Description", validators=[DataRequired()])
    photo = FileField(validators = [FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Only images allowed!')])

