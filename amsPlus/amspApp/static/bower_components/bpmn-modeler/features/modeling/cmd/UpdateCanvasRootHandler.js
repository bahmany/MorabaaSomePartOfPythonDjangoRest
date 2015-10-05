'use strict';

var Collections = require('diagram-js/lib/util/Collections');


function UpdateCanvasRootHandler(canvas, modeling) {
  this._canvas = canvas;
  this._modeling = modeling;
}

UpdateCanvasRootHandler.$inject = [ 'canvas', 'modeling' ];

module.exports = UpdateCanvasRootHandler;


UpdateCanvasRootHandler.prototype.execute = function(context) {

  var canvas = this._canvas;

  var newRoot = context.newRoot,
      newRootBusinessObject = newRoot.businessObject,
      oldRoot = canvas.getRootElement(),
      oldRootBusinessObject = oldRoot.businessObject,
      bpmnDefinitions = oldRootBusinessObject.$parent,
      diPlane = oldRootBusinessObject.di;

  // (1) replace process old <> new root
  canvas.setRootElement(newRoot, true);

  // (2) update root elements
  Collections.add(bpmnDefinitions.rootElements, newRootBusinessObject);
  newRootBusinessObject.$parent = bpmnDefinitions;

  Collections.remove(bpmnDefinitions.rootElements, oldRootBusinessObject);
  oldRootBusinessObject.$parent = null;

  // (3) wire di
  oldRootBusinessObject.di = null;

  diPlane.bpmnElement = newRootBusinessObject;
  newRootBusinessObject.di = diPlane;

  context.oldRoot = oldRoot;
};


UpdateCanvasRootHandler.prototype.revert = function(context) {

  var canvas = this._canvas;

  var newRoot = context.newRoot,
      newRootBusinessObject = newRoot.businessObject,
      oldRoot = context.oldRoot,
      oldRootBusinessObject = oldRoot.businessObject,
      bpmnDefinitions = newRootBusinessObject.$parent,
      diPlane = newRootBusinessObject.di;

  // (1) replace process old <> new root
  canvas.setRootElement(oldRoot, true);

  // (2) update root elements
  Collections.remove(bpmnDefinitions.rootElements, newRootBusinessObject);
  newRootBusinessObject.$parent = null;

  Collections.add(bpmnDefinitions.rootElements, oldRootBusinessObject);
  oldRootBusinessObject.$parent = bpmnDefinitions;

  // (3) wire di
  newRootBusinessObject.di = null;

  diPlane.bpmnElement = oldRootBusinessObject;
  oldRootBusinessObject.di = diPlane;
};