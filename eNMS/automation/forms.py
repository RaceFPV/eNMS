from flask_wtf import FlaskForm
from wtforms import (
    HiddenField,
    IntegerField,
    TextField,
    SelectField,
    SelectMultipleField
)


class ServiceForm(FlaskForm):
    id = HiddenField()
    name = TextField()
    description = TextField()
    devices = SelectMultipleField(choices=())
    pools = SelectMultipleField(choices=())
    waiting_time = IntegerField(default=0)


class CompareLogsForm(FlaskForm):
    first_version = SelectField(choices=())
    second_version = SelectField(choices=())


class AddJobForm(FlaskForm):
    job = SelectField()


class WorkflowCreationForm(FlaskForm):
    id = HiddenField()
    name = TextField()
    description = TextField()
    vendor = TextField()
    operating_system = TextField()
    devices = SelectMultipleField(choices=())
    pools = SelectMultipleField(choices=())


class WorkflowBuilderForm(FlaskForm):
    workflow = SelectField()
