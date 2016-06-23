clouderp.define('web_kanban.compatibility', function (require) {
"use strict";

var kanban_widgets = require('web_kanban.widgets');
var KanbanRecord = require('web_kanban.Record');
var KanbanColumn = require('web_kanban.Column');
var KanbanView = require('web_kanban.KanbanView');

return;
gce = window.gce || {};
gce.web_kanban = gce.web_kanban || {};
gce.web_kanban.AbstractField = kanban_widgets.AbstractField;
gce.web_kanban.KanbanGroup = KanbanColumn;
gce.web_kanban.KanbanRecord = KanbanRecord;
gce.web_kanban.KanbanView = KanbanView;

});
