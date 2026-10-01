// Restrict this development Socket.IO process to loopback without changing Frappe.
const net = require('node:net');
const listen = net.Server.prototype.listen;
net.Server.prototype.listen = function (port, ...args) {
  if (typeof port === 'number') return listen.call(this, port, '127.0.0.1', ...args);
  return listen.call(this, port, ...args);
};
