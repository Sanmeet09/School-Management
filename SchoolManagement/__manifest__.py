{
    'name': 'School Management',
    'version': '1.1',
    'sequence': 1,
    'author': 'Planet Odoo',
    'description': """Module for SchoolManagement""",
    'category': '',
    'website': '',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'wizards/students_wizard_view.xml',
        'views/students_details_view.xml',
        'views/teachers_details_view.xml',
        'views/different_school.xml',

    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
