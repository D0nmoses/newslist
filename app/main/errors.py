from flask import render_template
from . import main


@main.app_errorhandler(404)
def four_Ow_four(error):
    """
	Renders the 404 error page
	:param error: 
	:return: the rendered template
	"""""
    return render_template('4_0_4.html'), 404
