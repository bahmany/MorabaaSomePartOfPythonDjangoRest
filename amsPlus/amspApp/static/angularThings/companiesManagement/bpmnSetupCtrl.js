'use strict';
var amftest;
angular.module('AniTheme')
    .controller('bpmnSetupCtrl', function ($scope, $http, $translate, $rootScope, $state, $stateParams, $location, $modal, bpmnService) {
        $scope.bpmn = {};
        $scope.processObjs = [];
        $scope.charts = [];
        $scope.users = [];
        $scope.chartSelected = '';
        $scope.userSelected = '';
        $scope.form = {};
        $scope.usertask = {};
        $scope.lastSelected = {};
        $scope.properties = {};
        $scope.properties.convdive = '';
        $scope.activeElement = {};
        $scope.activeElementIsDef = '';
        $scope.companyId = $stateParams.companyid;
        //$scope.processId= $stateParams.processId;

        var viewer;
        viewer = new BpmnModule({container: '#bpmn-viewer'});
        $scope.showBpmn = function () {
            bpmnService.retrieveBpmn($stateParams.companyid,$stateParams.processId).success(function (data) {
                $scope.bpmn = data;
                $scope.processObjs = $scope.bpmn.processObjs;

                viewer.importXML($scope.bpmn.xml, function (err) {
                    $("#bpmn-viewer").fadeIn(150);


                    if (err) {
                        console.log('error rendering', err);
                    }
                });
            });
        };
        //function getFromRec(data) {
        //    data.children.forEach(function (chart, index) {
        //        $scope.charts.push({'id': chart.id, 'title': chart.name});
        //        if (chart.hasOwnProperty('children')) {
        //            if (chart.children.length >= 1) {
        //                getFromRec(chart);
        //            }
        //        }
        //    });
        //}

        $scope.listCharts = function (companyId) {
            bpmnService.listCharts(companyId).success(function (data) {
                $scope.charts = data;
                $scope.charts.results.shift();
            });
        };
        $scope.listUsers = function (companyId, chartId) {
            bpmnService.listUsers(companyId, chartId).success(function (data) {
                $scope.users = data;
            });
        };

        $scope.$watch("chartSelected", function (newVal, oldVal) {
            $scope.listUsers($scope.bpmn.company_id, newVal);
        });
        $scope.showBpmn();

        $scope.setupExclusive = function (exclusiveElement) {
            $scope.activeElement = exclusiveElement;
            amftest = $scope.activeElement;
            var moddle = new BpmnModdle();
            moddle.fromXML($scope.bpmn.xml, function (err, definitions) {
                definitions.get('rootElements')[0].flowElements.some(function (element, index, array) {
                    if (element.id == exclusiveElement.id) {
                        $scope.$apply(function () {
                            $scope.activeElementIsDef = element.default;
                            $scope.properties.convdive = element.get('gatewayDirection');
                            $scope.properties.outgoingSeq = element.outgoing;

                        });
                        $scope.properties.outgoingSeq.some(function (seq, index, array) {
                            if (seq.conditionExpression != undefined) {
                                $('#' + seq.id).val(seq.conditionExpression.body);
                            }
                        });
                        return true;
                    } else {
                        return false;
                    }
                });

                $("#bpmn-viewer").fadeOut(200);
                $('#exclusive-setup-div').fadeIn(200);
            });
        };

        $scope.saveSetupExclusive = function () {
            var moddle = new BpmnModdle();

            moddle.fromXML($scope.bpmn.xml, function (err, definitions) {

                definitions.get('rootElements')[0].flowElements.some(function (element, index, array) {
                    $scope.properties.outgoingSeq.some(function (seq, index, array) {
                        if (element.id == seq.id) {
                            element.conditionExpression = moddle.create('bpmn:FormalExpression', {body: $('#' + seq.id).val()});
                            return true;
                        } else {
                            return false;
                        }
                    });

                    if ($scope.activeElement.id == element.id) {

                        element.set('default', $('#isdef option:selected').val());
                        element.set('gatewayDirection', $('#convdive option:selected').val());

                    }


                });
                moddle.toXML(definitions, function (err, xmlStrUpdated) {
                    $scope.bpmn.xml = xmlStrUpdated;
                });
                bpmnService.bpmnUpdate($stateParams.companyid,$scope.bpmn.id, $scope.bpmn).success(function (data) {
                    $scope.bpmn = data;

                    $('#exclusive-setup-div').fadeOut(200);
                    $("#bpmn-viewer").fadeIn(200);
                    viewer.importXML($scope.bpmn.xml, function (err) {

                        if (err) {
                            console.log('error rendering', err);
                        }
                    });
                });
            });
        };

        $scope.setupParallel = function (parallelElement) {
            $scope.activeElement = parallelElement;

            $("#bpmn-viewer").fadeOut(200);
            $('#parallel-setup-div').fadeIn(200);
            var moddle = new BpmnModdle();
            moddle.fromXML($scope.bpmn.xml, function (err, definitions) {
                definitions.get('rootElements')[0].flowElements.some(function (element, index, array) {
                    if (element.id == parallelElement.id) {
                        $scope.properties.convdive = element.get('gatewayDirection');

                        return true;
                    } else {
                        return false;
                    }
                });
            });
        };
        $scope.saveSetupParallel = function () {
            var moddle = new BpmnModdle();
            moddle.fromXML($scope.bpmn.xml, function (err, definitions) {
                definitions.get('rootElements')[0].flowElements.some(function (element, index, array) {
                    if (element.id == $scope.activeElement.id) {
                        element.set('gatewayDirection', $('#convdive option:selected').val());
                        return true;
                    } else {
                        return false;
                    }
                });
                moddle.toXML(definitions, function (err, xmlStrUpdated) {
                    $scope.bpmn.xml = xmlStrUpdated;
                });
                bpmnService.bpmnUpdate($stateParams.companyid,$scope.bpmn.id, $scope.bpmn).success(function (data) {
                    $('#parallel-setup-div').fadeOut(200);
                    $("#bpmn-viewer").fadeIn(200);
                    viewer.importXML($scope.bpmn.xml, function (err) {

                        if (err) {
                            console.log('error rendering', err);
                        }
                    });
                });
            });

        };

        $scope.setupManualTask = function (manualTaskElement) {
            $scope.activeElement = manualTaskElement;

            var moddle = new BpmnModdle();
            moddle.fromXML($scope.bpmn.xml, function (err, definitions) {
                definitions.get('rootElements')[0].flowElements.some(function (element, index, array) {
                    if (element.id == $scope.activeElement.id) {
                        $scope.$apply(function () {
                            $scope.activeElement.isForCompensation = element.get('isForCompensation');
                        });
                        return true;
                    } else {
                        return false;
                    }
                });
            });


            var isExistFlag = 0;
            if ($scope.bpmn.form == null) {
                $scope.bpmn.form = [];
            }
            if ($scope.bpmn.processObjs == null) {
                $scope.bpmn.processObjs = [];
            }
            $scope.bpmn.form.some(function (element, index, array) {

                if (element["bpmnObjID"] == manualTaskElement.id) {
                    $scope.form = angular.copy(element);
                    isExistFlag = 1;
                    return true
                } else {
                    return false
                }
            });
            if (isExistFlag == 0) {
                $scope.form.bpmnID = $scope.bpmn.id;
                $scope.form.bpmnObjID = manualTaskElement.id;

                if ($scope.lastSelected != manualTaskElement) {
                    $scope.form.schema = {'fields': []};
                }
            }


            $("#bpmn-viewer").fadeOut(200);
            $('#manualtask-setup-div').fadeIn(200);

            $scope.$apply(function () {

                $scope.lastSelected = manualTaskElement;
            });
        };

        $scope.setupUserTask = function (userTaskElement) {
            $scope.activeElement = userTaskElement;
            if ($scope.bpmn.userTasks == null) {
                $scope.bpmn.userTasks = [];
            }
            $scope.bpmn.userTasks.forEach(function (element) {

                if (element.taskId == userTaskElement.id) {
                    $scope.chartSelected = element.chartPerformer;
                    $scope.userSelected = element.performer;
                }
            });
            $scope.listCharts($scope.bpmn.company_id);

            var moddle = new BpmnModdle();
            moddle.fromXML($scope.bpmn.xml, function (err, definitions) {
                definitions.get('rootElements')[0].flowElements.some(function (element, index, array) {
                    if (element.id == $scope.activeElement.id) {
                        $scope.$apply(function () {
                            $scope.activeElement.isForCompensation = element.get('isForCompensation');
                        });
                        return true;
                    } else {
                        return false;
                    }
                });
            });


            var isExistFlag = 0;
            if ($scope.bpmn.form == null) {
                $scope.bpmn.form = [];
            }
            if ($scope.bpmn.processObjs == null) {
                $scope.bpmn.processObjs = [];
            }
            $scope.bpmn.form.some(function (element, index, array) {

                if (element["bpmnObjID"] == userTaskElement.id) {
                    $scope.form = angular.copy(element);
                    isExistFlag = 1;
                    return true
                } else {
                    return false
                }
            });
            if (isExistFlag == 0) {
                $scope.form.bpmnID = $scope.bpmn.id;
                $scope.form.bpmnObjID = userTaskElement.id;

                if ($scope.lastSelected != userTaskElement) {
                    $scope.form.schema = {'fields': []};
                }
            }


            $("#bpmn-viewer").fadeOut(200);
            $('#usertask-setup-div').fadeIn(200);

            $scope.$apply(function () {

                $scope.lastSelected = userTaskElement;
            });
        };
        $scope.setupTask = function (taskElement) {

            var isExistFlag = 0;
            if ($scope.bpmn.form == null) {
                $scope.bpmn.form = [];
            }
            if ($scope.bpmn.processObjs == null) {
                $scope.bpmn.processObjs = [];
            }
            $scope.bpmn.form.some(function (element, index, array) {

                if (element["bpmnObjID"] == taskElement.id) {
                    $scope.form =angular.copy(element);
                    isExistFlag = 1;
                    return true
                } else {
                    return false
                }
            });
            if (isExistFlag == 0) {
                $scope.form.bpmnID = $scope.bpmn.id;
                $scope.form.bpmnObjID = taskElement.id;

                if ($scope.lastSelected != taskElement) {
                    $scope.form.schema = {'fields': []};
                }
            }


            $("#bpmn-viewer").fadeOut(200);
            $('#task-setup-div').fadeIn(200);

            $scope.$apply(function () {

                $scope.lastSelected = taskElement;
            });
        };

        $scope.removeProcessObj = function (index) {
            var item = $scope.processObjs[index];

            $scope.bpmn.form.forEach(function (form) {
                form.schema.fields.forEach(function (field, index) {

                    if (field["name"] == item["name"]) {
                        form.schema.fields.splice(index, 1);
                    }
                });

            });
            $scope.processObjs.splice(index, 1);
            $scope.bpmn.processObjs = $scope.processObjs;
            bpmnService.bpmnUpdate($stateParams.companyid,$scope.bpmn.id, $scope.bpmn).success(function (data) {
                $scope.bpmn = data;
            });
        };
        $scope.saveSetupManualTask = function () {
            if ($scope.processObjs == null) {
                $scope.processObjs = [];
            }
            var moddle = new BpmnModdle();
            moddle.fromXML($scope.bpmn.xml, function (err, definitions) {
                definitions.get('rootElements')[0].flowElements.some(function (element, index, array) {
                    if (element.id == $scope.activeElement.id) {
                        element.set('isForCompensation', $scope.activeElement.isForCompensation);
                        return true;
                    } else {
                        return false;
                    }
                });
                moddle.toXML(definitions, function (err, xmlStrUpdated) {
                    $scope.bpmn.xml = xmlStrUpdated;
                });
                $scope.form.schema.fields.forEach(function (obj, index) {

                    var currentIndex;
                    var searchableStr = '';
                    //In this If else app add new form objects to $scope.processObjs
                    if (obj.name.indexOf('__') != -1) {
                        $scope.processObjs.forEach(function (obj2) {
                            if (obj2.hasOwnProperty('$_isDragging')) {
                                delete(obj2.$_isDragging);
                            }
                            searchableStr += JSON.stringify(obj2);
                        });
                        currentIndex = searchableStr.indexOf(obj.name);
                        if (currentIndex == -1) {
                            $scope.processObjs.push(obj);
                        }
                    } else {
                        obj.name = $scope.lastSelected.id + '__' + obj.name;
                        searchableStr = '';
                        $scope.processObjs.forEach(function (obj2) {
                            if (obj2.hasOwnProperty('$_isDragging')) {
                                delete(obj2.$_isDragging);
                            }
                            searchableStr += JSON.stringify(obj2);
                        });
                        currentIndex = searchableStr.indexOf(obj.name);
                        if (currentIndex == -1) {
                            $scope.processObjs.push(obj);
                        }
                    }
                    $scope.bpmn.processObjs = $scope.processObjs;

                });
                 var isUpdateFlag = 0;
                    // In this if check if bpmn has any form then update bpmn.form with new data or add new form to it
                    if ($scope.bpmn.form != null) {
                        $scope.bpmn.form.some(function (element, index, array) {
                            if (element["bpmnObjID"] == $scope.form.bpmnObjID) {
                                $scope.bpmn.form[index] = angular.copy($scope.form);

                                isUpdateFlag = 1;
                                return true
                            } else {
                                return false
                            }
                        });
                    } else {
                        $scope.bpmn.form = []
                    }
                    if (isUpdateFlag == 0) {
                        $scope.bpmn.form.push($scope.form);
                    }
                bpmnService.bpmnUpdate($stateParams.companyid,$scope.bpmn.id, $scope.bpmn).success(function (data) {
                    $scope.bpmn = data;
                    $('#manualtask-setup-div').fadeOut(200);
                    $("#bpmn-viewer").fadeIn(200);
                    viewer.importXML($scope.bpmn.xml, function (err) {

                        if (err) {
                            console.log('error rendering', err);
                        }
                    });
                });
            });

        };
        $scope.saveSetupUserTask = function () {
            if ($scope.processObjs == null) {
                $scope.processObjs = [];
            }
            var moddle = new BpmnModdle();
            moddle.fromXML($scope.bpmn.xml, function (err, definitions) {
                definitions.get('rootElements')[0].flowElements.some(function (element, index, array) {
                    if (element.id == $scope.activeElement.id) {
                        element.set('isForCompensation', $scope.activeElement.isForCompensation);

                        return true;
                    } else {
                        return false;
                    }
                });
                moddle.toXML(definitions, function (err, xmlStrUpdated) {
                    $scope.bpmn.xml = xmlStrUpdated;

                });


                $scope.usertask.taskId = $scope.activeElement.id;
                $scope.usertask.performer = $scope.userSelected;
                $scope.usertask.chartPerformer = $scope.chartSelected;

                if ($scope.bpmn.userTasks == null) {
                    $scope.bpmn.userTasks = [];
                }
                var upFlag = 0;
                $scope.bpmn.userTasks.some(function (element, index, array) {

                    if ($scope.usertask.taskId == element.taskId) {
                        upFlag = 1;
                        $scope.bpmn.userTasks[index] = angular.copy($scope.usertask);
                        $scope.usertask = {};
                        return true;
                    } else {
                        return false;
                    }
                });
                if (upFlag == 0) {
                    $scope.bpmn.userTasks.push($scope.usertask);
                }
                var isUpdateFlag = 0;
                $scope.form.schema.fields.forEach(function (obj, index) {


                    var currentIndex;
                    var searchableStr = '';
                    //In this If else app add new form objects to $scope.processObjs
                    if (obj.name.indexOf('__') != -1) {
                        $scope.processObjs.forEach(function (obj2, index) {
                            if (obj2.hasOwnProperty('$_isDragging')) {
                                delete($scope.processObjs[index].$_isDragging);
                            }
                            searchableStr += JSON.stringify(obj2);
                        });
                        currentIndex = searchableStr.indexOf(obj.name);
                        if (currentIndex == -1) {
                            $scope.processObjs.push(obj);
                        }
                    }
                    else {
                        obj.name = $scope.lastSelected.id + '__' + obj.name;
                        searchableStr = '';
                        $scope.processObjs.forEach(function (obj2) {
                            searchableStr += JSON.stringify(obj2);
                        });
                        currentIndex = searchableStr.indexOf(obj.name);
                        if (currentIndex == -1) {
                            $scope.processObjs.push(obj);
                        }
                    }


                    $scope.bpmn.processObjs = $scope.processObjs;

                });

                    // In this if check if bpmn has any form then update bpmn.form with new data or add new form to it
                    if ($scope.bpmn.form == null) {
                        $scope.bpmn.form = []
                    }
                    $scope.bpmn.form.some(function (element, index, array) {
                        if (element["bpmnObjID"] == $scope.form.bpmnObjID) {
                            $scope.bpmn.form[index] = angular.copy($scope.form);

                            isUpdateFlag = 1;
                            return true
                        } else {
                            return false
                        }
                    });

                    if (isUpdateFlag == 0) {
                        $scope.bpmn.form.push($scope.form);
                    }
                bpmnService.bpmnUpdate($stateParams.companyid,$scope.bpmn.id, $scope.bpmn).success(function (data) {
                    $('#usertask-setup-div').fadeOut(200);
                    $("#bpmn-viewer").fadeIn(200);
                    $scope.bpmn = data;
                    viewer.importXML($scope.bpmn.xml, function (err) {
                        if (err) {
                            console.log('error rendering', err);
                        }
                    });
                });
            });

        };
        $scope.saveSetupTask = function () {
            if ($scope.processObjs == null) {
                $scope.processObjs = [];
            }
            var isUpdateFlag = 0;
            $scope.form.schema.fields.forEach(function (obj, index) {
                var currentIndex;
                var searchableStr = '';
                //In this If else app add new form objects to $scope.processObjs
                if (obj.name.indexOf('__') != -1) {
                    $scope.processObjs.forEach(function (obj2) {
                        if (obj2.hasOwnProperty('$_isDragging')) {
                            delete(obj2.$_isDragging);
                        }
                        searchableStr += JSON.stringify(obj2);
                    });
                    currentIndex = searchableStr.indexOf(obj.name);
                    if (currentIndex == -1) {
                        $scope.processObjs.push(obj);
                    }
                } else {
                    obj.name = $scope.lastSelected.id + '__' + obj.name;
                    searchableStr = '';
                    $scope.processObjs.forEach(function (obj2) {
                            if (obj2.hasOwnProperty('$_isDragging')) {
                                delete(obj2.$_isDragging);
                            }
                            searchableStr += JSON.stringify(obj2);
                        }
                    )
                    ;
                    currentIndex = searchableStr.indexOf(obj.name);
                    if (currentIndex == -1) {
                        $scope.processObjs.push(obj);
                    }
                }

                // In this if check if bpmn has any form then update bpmn.form with new data or add new form to it


                $scope.bpmn.processObjs = $scope.processObjs;

            });
            if ($scope.bpmn.form != null) {
                $scope.bpmn.form.some(function (element, index, array) {
                    if (element["bpmnObjID"] == $scope.form.bpmnObjID) {
                        $scope.bpmn.form[index] = angular.copy($scope.form);
                        isUpdateFlag = 1;
                        return true
                    } else {
                        return false
                    }
                });
            } else {
                $scope.bpmn.form = []
            }
            if (isUpdateFlag == 0) {
                $scope.bpmn.form.push($scope.form);
            }
            bpmnService.bpmnUpdate($stateParams.companyid,$scope.bpmn.id, $scope.bpmn).success(function (data) {
                $scope.bpmn = data;
                $('#task-setup-div').fadeOut(200);
                $("#bpmn-viewer").fadeIn(200);
            });

        };

        $scope.cancelForm = function () {
            $('#task-setup-div').fadeOut(200);
            $("#bpmn-viewer").fadeIn(200);
        };

        $scope.cancelSetupParallel = function () {
            $('#parallel-setup-div').fadeOut(200);
            $("#bpmn-viewer").fadeIn(200);
        };
        $scope.cancelSetupManualTask = function () {
            $('#manualtask-setup-div').fadeOut(200);
            $("#bpmn-viewer").fadeIn(200);
        };

        $scope.cancelSetupUserTask = function () {
            $('#usertask-setup-div').fadeOut(200);
            $("#bpmn-viewer").fadeIn(200);
        };

        $scope.cancelSetupExclusive = function () {
            $('#exclusive-setup-div').fadeOut(200);
            $("#bpmn-viewer").fadeIn(200);
        };

        $scope.resetForm = function () {
            $scope.form.schema = {'fields': []};
        };


        viewer.on('element.click', function (event) {

            if (event.element.type == 'bpmn:Task') {
                $scope.setupTask(event.element);
            }

            if (event.element.type == 'bpmn:ParallelGateway') {
                $scope.setupParallel(event.element);
            }
            if (event.element.type == 'bpmn:ExclusiveGateway') {
                $scope.setupExclusive(event.element);
            }
            if (event.element.type == 'bpmn:ManualTask') {
                $scope.setupManualTask(event.element);
            }
            if (event.element.type == 'bpmn:UserTask') {
                $scope.setupUserTask(event.element);
            }
        });

    })
;
