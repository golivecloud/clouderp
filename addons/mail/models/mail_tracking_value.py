from datetime import datetime

from gce import api, fields, models, tools


class MailTracking(models.Model):
    _name = 'mail.tracking.value'
    _description = 'Mail Tracking Value'

    field = fields.Char('Changed Field', required=True, readonly=1)
    field_desc = fields.Char('Field Description', required=True, readonly=1)
    field_type = fields.Char('Field Type')

    old_value_integer = fields.Integer('Old Value Integer', readonly=1)
    old_value_float = fields.Float('Old Value Float', readonly=1)
    old_value_monetary = fields.Float('Old Value Monetary', readonly=1)
    old_value_char = fields.Char('Old Value Char', readonly=1)
    old_value_text = fields.Text('Old Value Text', readonly=1)
    old_value_datetime = fields.Datetime('Old Value DateTime', readonly=1)

    new_value_integer = fields.Integer('New Value Integer', readonly=1)
    new_value_float = fields.Float('New Value Float', readonly=1)
    new_value_monetary = fields.Float('New Value Monetary', readonly=1)
    new_value_char = fields.Char('New Value Char', readonly=1)
    new_value_text = fields.Text('New Value Text', readonly=1)
    new_value_datetime = fields.Datetime('New Value Datetime', readonly=1)

    mail_message_id = fields.Many2one('mail.message', 'Message ID', required=True, select=True, ondelete='cascade')

    @api.model
    def create_tracking_values(self, initial_value, new_value, col_name, col_info):
        tracked = True
        values = {'field': col_name, 'field_desc': col_info['string'], 'field_type': col_info['type']}

        if col_info['type'] in ['integer', 'float', 'char', 'text', 'datetime', 'monetary']:
            values.update({
                'old_value_%s' % col_info['type']: initial_value,
                'new_value_%s' % col_info['type']: new_value
            })
        elif col_info['type'] == 'date':
            values.update({
                'old_value_datetime': initial_value and datetime.strftime(datetime.combine(datetime.strptime(initial_value, tools.DEFAULT_SERVER_DATE_FORMAT), datetime.min.time()), tools.DEFAULT_SERVER_DATETIME_FORMAT) or False,
                'new_value_datetime': new_value and datetime.strftime(datetime.combine(datetime.strptime(new_value, tools.DEFAULT_SERVER_DATE_FORMAT), datetime.min.time()), tools.DEFAULT_SERVER_DATETIME_FORMAT) or False,
            })
        elif col_info['type'] == 'boolean':
            values.update({
                'old_value_integer': initial_value,
                'new_value_integer': new_value
            })
        elif col_info['type'] == 'selection':
            values.update({
                'old_value_char': initial_value and dict(col_info['selection'])[initial_value] or '',
                'new_value_char': new_value and dict(col_info['selection'])[new_value] or ''
            })
        elif col_info['type'] == 'many2one':
            values.update({
                'old_value_integer': initial_value and initial_value.id or 0,
                'new_value_integer': new_value and new_value.id or 0,
                'old_value_char': initial_value and initial_value.name_get()[0][1] or '',
                'new_value_char': new_value and new_value.name_get()[0][1] or ''
            })
        else:
            tracked = False

        if tracked:
            return values
        return {}

    @api.multi
    def get_old_display_value(self):
        result = []
        for record in self:
            if record.field_type in ['integer', 'float', 'char', 'text', 'datetime', 'monetary']:
                result.append(getattr(record, 'old_value_%s' % record.field_type))
            elif record.field_type == 'date':
                if record.old_value_datetime:
                    old_date = datetime.strptime(record.old_value_datetime, tools.DEFAULT_SERVER_DATETIME_FORMAT).date()
                    result.append(old_date.strftime(tools.DEFAULT_SERVER_DATE_FORMAT))
                else:
                    result.append(record.old_value_datetime)
            elif record.field_type == 'boolean':
                result.append(bool(record.old_value_integer))
            elif record.field_type in ['many2one', 'selection']:
                result.append(record.old_value_char)
            else:
                result.append(record.old_value_char)
        return result

    @api.multi
    def get_new_display_value(self):
        result = []
        for record in self:
            if record.field_type in ['integer', 'float', 'char', 'text', 'datetime', 'monetary']:
                result.append(getattr(record, 'new_value_%s' % record.field_type))
            elif record.field_type == 'date':
                if record.new_value_datetime:
                    new_date = datetime.strptime(record.new_value_datetime, tools.DEFAULT_SERVER_DATETIME_FORMAT).date()
                    result.append(new_date.strftime(tools.DEFAULT_SERVER_DATE_FORMAT))
                else:
                    result.append(record.new_value_datetime)
            elif record.field_type == 'boolean':
                result.append(bool(record.new_value_integer))
            elif record.field_type in ['many2one', 'selection']:
                result.append(record.new_value_char)
            else:
                result.append(record.new_value_char)
        return result
