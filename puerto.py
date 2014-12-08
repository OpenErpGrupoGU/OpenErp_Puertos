
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
class personas_pr(osv.osv):

    _name = 'personas.pr'
    _description = 'personas.pr'
    _rec_name='dni'
    _columns = {
            'nombre':fields.char('Nombre', size = 50, required = True, readonly = False),
            'dni':fields.char('DNI', size = 10, required = True, readonly = False),
            'direccion':fields.char('Dirección', size = 50, required = True, readonly = False),
            'salida_tripulacion':fields.many2many('salidas.pr', 'sal_per_tripulacion', 'dni_persona', 'codigo_salida', 'Tripula en'),
            'salida_personas_embarcar':fields.many2many('salidas.pr', 'sal_per_embarcar', 'dni_persona', 'codigo_salida', 'Pasajero en'),
        }
personas_pr()

class barcos_pr(osv.osv):

    _name = 'barcos.pr'
    _description = 'barcos.pr'
    _rec_name='matricula'
    _columns = {
            'matricula':fields.char('Matricula', size = 50, required = True, readonly = False),
            'nombre':fields.char('Nombre', size = 30, required = True, readonly = False),
            'tipo':fields.selection([
                ('pesca','Barco de pesca'),
                ('mercante','Barco mercante'),
                ('crucero','Crucero'),
                ('velero','Velero'),
                 ],'Tipo de barco', select = False, readonly = False),
            'propietario': fields.many2one('personas.pr','Propietario', required = True, readonly = False),
            'muelle':fields.char('Muelle', size = 5, required = True, readonly = False),
            'darsena':fields.char('Dársena', size = 5, required = True, readonly = False),
            'cuota':fields.float('Cuota', digits = (6,2), required = True, readonly = False),
            'periodicidad':fields.selection([
                ('mensual','Mensual'),
                ('trimestral','Trimestral'),
                ('anual','Anual'),
                 ],'Periocidad de cuota', select = False, readonly = False),
        }
barcos_pr()


class salidas_pr(osv.osv):

    _name = 'salidas.pr'
    _description = 'salidas.pr'
    _rec_name='codigo'
    _columns = {
            'codigo':fields.char('Código', size = 10, required = True, readonly = False),
            'barco': fields.many2one('barcos.pr','Barco', required = True, readonly = False),
            'fecha': fields.date('Fecha', required = True, readonly = False),
            'hora': fields.float('Hora', required = True, readonly = False),
            #'hora': fields.time('Hora', required = True, readonly = False),
            'destino':fields.char('Destino', size = 30, required = True, readonly = False),
            'patron': fields.many2one('personas.pr','Patrón', required = True, readonly = False),
            'tripulacion':fields.many2many('personas.pr', 'sal_per_tripulacion', 'codigo_salida', 'dni_persona', 'Tripulación'),
            'personas_embarcar':fields.many2many('personas.pr', 'sal_per_embarcar', 'codigo_salida', 'dni_persona', 'Pasajeros'),
        }
salidas_pr()
