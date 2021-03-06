# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2009  Renato Lima - Akretion                                  #
#                                                                             #
#This program is free software: you can redistribute it and/or modify         #
#it under the terms of the GNU Affero General Public License as published by  #
#the Free Software Foundation, either version 3 of the License, or            #
#(at your option) any later version.                                          #
#                                                                             #
#This program is distributed in the hope that it will be useful,              #
#but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#GNU Affero General Public License for more details.                          #
#                                                                             #
#You should have received a copy of the GNU Affero General Public License     #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
###############################################################################

{
    'name': 'Brazilian Localisation Data Extension for Account',
    'description': 'Brazilian Localisation Data Extension for Account',
    'license': 'AGPL-3',
    'author': 'Akretion, OpenERP Brasil',
    'version': '0.1',
    'depends': [
        'l10n_br_account',
    ],
    'data': [
        'account.product.fiscal.classification.template.csv',
        'l10n_br_account.cnae.csv',
        'l10n_br_account.service.type.csv',
        'l10n_br_data_account_data.xml',
        'account_fiscal_position_rule_data.xml',
    ],
    'demo': [
        'l10n_br_data_account_demo.xml',
    ],
    'category': 'Localisation',
    'active': False,
    'installable': True
}
