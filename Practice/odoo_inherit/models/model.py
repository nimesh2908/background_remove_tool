from odoo import  fields, models, api
from odoo.exceptions import ValidationError

class Car_Inheritance(models.Model):
	_name = 'car.inherit'
	_description = "Inherit Data Of Car"
	_inherit = 'car'

	km = fields.Integer(string = "Kilometers")