clouderp.define('web.session', function (require) {
    var Session = require('web.Session');
    var modules = clouderp._modules;
    return new Session(undefined, undefined, {modules:modules, use_cors: false});
});
