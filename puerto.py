
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP , Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import fields, osv
class vendedores_as(osv.osv):

    _name = 'vendedores.as'
    _description = 'vendedores.as'
    _rec_name='dni'
    _columns = {
            'nombre':fields.char('Nombre', size = 30, required = True, readonly = False),
            'apellidos':fields.char('Apellidos', size = 30, required = True, readonly = False),
            'dni':fields.char('DNI Vendedor', size = 10, required = True, readonly = False),
            'telefono':fields.char('Telefono', size = 15, required = True, readonly = False),
            'imagen':fields.binary('Imagen', filters=None), 
            'automovil':fields.one2many('automoviles.as', 'vendedor', 'Automovil', required=False),
        }
vendedores_as()