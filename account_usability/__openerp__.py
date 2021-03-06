# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Accoount Usability Improvements',
    'version': '9.0.1.10.0',
    'category': 'Accounting',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'account',
        # por método get_model_id_and_name
        'account_reports',
        "payment",
        # para agregar boton en move lines de payment group
        # TODO deberiamos evitar esta dependencia y hacer que
        # payment group herede de move line
        "account_payment_group",
    ],
    'data': [
        'views/account_journal_view.xml',
        'views/account_payment_term_view.xml',
        'views/payment_acquirer_view.xml',
        'views/account_invoice_view.xml',
        'views/account_bank_statement_view.xml',
        'views/account_move_line_view.xml',
        'views/account_analytic_view.xml',
        'data/account_payment_method_data.xml',
        'data/mail_data.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    # lo hacemos auto install porque este repo no lo podemos agregar en otros
    # por build de travis (ej sipreco) y queremos que para runbot se auto
    # instale
    'auto_install': True,
    'application': False,
}
