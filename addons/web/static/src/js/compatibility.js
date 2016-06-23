// ------------------------------------------------------------------------------
// Compatibility with clouderp v8.  
// 
// With the new module system, no global variable can (and should) be accessed
// in gce.  This file exports everything, to mimic the previous global 
// namespace structure.  This is only supposed to be used by 3rd parties to 
// facilitate migration.  clouderp addons should not use the 'gce' variable at 
// all.
// ------------------------------------------------------------------------------
clouderp.define('web.compatibility', function (require) {
"use strict";

var ActionManager = require('web.ActionManager');
var core = require('web.core');
var data = require('web.data');
var Dialog = require('web.Dialog');
var FavoriteMenu = require('web.FavoriteMenu');
var form_common = require('web.form_common');
var formats = require('web.formats');
var FormView = require('web.FormView');
var form_relational = require('web.form_relational'); // necessary
var form_widgets = require('web.form_widgets'); // necessary
var framework = require('web.framework');
var ListView = require('web.ListView');
var Menu = require('web.Menu');
var Model = require('web.DataModel');
var pyeval = require('web.pyeval');
var Registry = require('web.Registry');
var SearchView = require('web.SearchView');
var session = require('web.session');
var Sidebar = require('web.Sidebar');
var SystrayMenu = require('web.SystrayMenu');
var time = require('web.time');
var UserMenu = require('web.UserMenu');
var utils = require('web.utils');
var View = require('web.View');
var ViewManager = require('web.ViewManager');
var WebClient = require('web.WebClient');
var Widget = require('web.Widget');

var client_started = $.Deferred();

var OldRegistry = Registry.extend({
    add: function (key, path) {
    },
    get_object: function (key) {
        return get_object(this.map[key]);
    },
});

window.gce = window.gce || {};

$.Mutex = utils.Mutex;
gce._session_id = "instance0";
gce._t = core._t;
gce.get_cookie = utils.get_cookie;

gce.qweb = core.qweb;
gce.session = session;

gce.web = gce.web || {};
gce.web._t = core._t;
gce.web._lt = core._lt;

gce.web.ActionManager = ActionManager;
gce.web.auto_str_to_date = time.auto_str_to_date;
gce.web.blockUI = framework.blockUI;
gce.web.BufferedDataSet = data.BufferedDataSet;
gce.web.bus = core.bus;
gce.web.Class = core.Class;
gce.web.client_actions = make_old_registry(core.action_registry);
gce.web.CompoundContext = data.CompoundContext;
gce.web.CompoundDomain = data.CompoundDomain;
gce.web.DataSetSearch = data.DataSetSearch;
gce.web.DataSet = data.DataSet;
gce.web.date_to_str = time.date_to_str;
gce.web.Dialog = Dialog;
gce.web.DropMisordered = utils.DropMisordered;

gce.web.form = gce.web.form || {};
gce.web.form.AbstractField = form_common.AbstractField;
gce.web.form.compute_domain = data.compute_domain;
gce.web.form.DefaultFieldManager = form_common.DefaultFieldManager;
gce.web.form.FieldChar = core.form_widget_registry.get('char');
gce.web.form.FieldFloat = core.form_widget_registry.get('float');
gce.web.form.FieldStatus = core.form_widget_registry.get('statusbar');
gce.web.form.FieldMany2ManyTags = core.form_widget_registry.get('many2many_tags');
gce.web.form.FieldMany2One = core.form_widget_registry.get('many2one');
gce.web.form.FormWidget = form_common.FormWidget;
gce.web.form.tags = make_old_registry(core.form_tag_registry);
gce.web.form.widgets = make_old_registry(core.form_widget_registry);
gce.web.form.custom_widgets = make_old_registry(core.form_custom_registry);

gce.web.format_value = formats.format_value;
gce.web.FormView = FormView;

gce.web.json_node_to_xml = utils.json_node_to_xml;

gce.web.ListView = ListView;
gce.web.Menu = Menu;
gce.web.Model = Model;
gce.web.normalize_format = time.strftime_to_moment_format;
gce.web.py_eval = pyeval.py_eval;
gce.web.pyeval = pyeval;
gce.web.qweb = core.qweb;

gce.web.Registry = OldRegistry;

gce.web.search = {};
gce.web.search.FavoriteMenu = FavoriteMenu;
gce.web.SearchView = SearchView;
gce.web.Sidebar = Sidebar;
gce.web.str_to_date = time.str_to_date;
gce.web.str_to_datetime = time.str_to_datetime;
gce.web.SystrayItems = SystrayMenu.Items;
gce.web.unblockUI = framework.unblockUI;
gce.web.UserMenu = UserMenu;
gce.web.View = View;
gce.web.ViewManager = ViewManager;
gce.web.views = make_old_registry(core.view_registry);
gce.web.WebClient = WebClient;
gce.web.Widget = Widget;

gce.Widget = gce.web.Widget;
gce.Widget.prototype.session = session;


WebClient.include({
    init: function () {
        gce.client = this;
        gce.webclient = this;
        start_modules();
        client_started.resolve();
        this._super.apply(this, arguments);
    },
});


function make_old_registry(registry) {
    return {
        add: function (key, path) {
            client_started.done(function () {
                registry.add(key, get_object(path));
            });
        },
    };
}
function get_object(path) {
    var object_match = gce;
    path = path.split('.');
    // ignore first section
    for(var i=1; i<path.length; ++i) {
        object_match = object_match[path[i]];
    }
    return object_match;
}

/**
 * gce instance constructor
 *
 * @param {Array|String} modules list of modules to initialize
 */
var inited = false;
function start_modules (modules) {
    if (modules === undefined) {
        modules = clouderp._modules;
    }
    modules = _.without(modules, "web");
    if (inited) {
        throw new Error("gce was already inited");
    }
    inited = true;
    for(var i=0; i < modules.length; i++) {
        var fct = gce[modules[i]];
        if (typeof(fct) === "function") {
            gce[modules[i]] = {};
            for (var k in fct) {
                gce[modules[i]][k] = fct[k];
            }
            fct(gce, gce[modules[i]]);
        }
    }
    gce._modules = ['web'].concat(modules);
    return gce;
};

// Monkey-patching of the ListView for backward compatibiliy of the colors and
// fonts row's attributes, as they are deprecated in 9.0.
ListView.include({
    load_list: function(data) {
        this._super(data);
        if (this.fields_view.arch.attrs.colors) {
            this.colors = _(this.fields_view.arch.attrs.colors.split(';')).chain()
                .compact()
                .map(function(color_pair) {
                    var pair = color_pair.split(':'),
                        color = pair[0],
                        expr = pair[1];
                    return [color, py.parse(py.tokenize(expr)), expr];
                }).value();
        }

        if (this.fields_view.arch.attrs.fonts) {
            this.fonts = _(this.fields_view.arch.attrs.fonts.split(';')).chain().compact()
                .map(function(font_pair) {
                    var pair = font_pair.split(':'),
                        font = pair[0],
                        expr = pair[1];
                    return [font, py.parse(py.tokenize(expr)), expr];
                }).value();
        }
    },
    /**
     * Returns the style for the provided record in the current view (from the
     * ``@colors`` and ``@fonts`` attributes)
     *
     * @param {Record} record record for the current row
     * @returns {String} CSS style declaration
     */
    style_for: function (record) {
        var len, style= '';

        var context = _.extend({}, record.attributes, {
            uid: session.uid,
            current_date: moment().format('YYYY-MM-DD')
            // TODO: time, datetime, relativedelta
        });
        var i;
        var pair;
        var expression;
        if (this.fonts) {
            for(i=0, len=this.fonts.length; i<len; ++i) {
                pair = this.fonts[i];
                var font = pair[0];
                expression = pair[1];
                if (py.PY_isTrue(py.evaluate(expression, context))) {
                    switch(font) {
                    case 'bold':
                        style += 'font-weight: bold;';
                        break;
                    case 'italic':
                        style += 'font-style: italic;';
                        break;
                    case 'underline':
                        style += 'text-decoration: underline;';
                        break;
                    }
                }
            }
        }
 
        if (!this.colors) { return style; }
        for(i=0, len=this.colors.length; i<len; ++i) {
            pair = this.colors[i];
            var color = pair[0];
            expression = pair[1];
            if (py.PY_isTrue(py.evaluate(expression, context))) {
                return style += 'color: ' + color + ';';
            }
        }
        return style;
     },
});


});
