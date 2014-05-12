(function($, window, document, undefined) {
	
	var $hash = window.location.hash;
	if ($hash) {
		//alert($hash);
		$('html,body').animate({scrollTop: 300 },'slow');
	}

  $(function() {
    // Tag IE10
    if((Function('/*@cc_on return document.documentMode===10@*/')()) || (Function('/*@cc_on return document.documentMode===11@*/')())) {
      $('html').addClass('ie10');
    }
    //SvgGrayscaleForIeTen.init('.ie10 .leadership-bio-list .flipper .leadership-bio-headshot');

    // Equal height columns
    $('[data-js="eqh-w"]').each(function() {
      var $self = $(this);
      if($.fn.imagesLoaded) {
        $(document).imagesLoaded(function() {
          $self.find('[data-js="eqh-c"]').equalHeights();
        });
      } else {
        $self.find('[data-js="eqh-c"]').equalHeights();
      }
    });

    $('.animated-percentage-graph').animatedPercentageGraph();
    window.setInterval(function() {
      $('.animated-percentage-graph').each(function() {
        $(this).data('apg').run();
      });
    }, 5000);

    $('.flipboard-counter').each(function() {
      var n = $(this).data('number');
      if(n) {
        var counter = $(this).FlipClock(n, {
          clockFace: 'counter',
          showCommas: true
        });
        var interval = window.setInterval(function() {
          counter.increment();
          /*if(counter.getTime().time == n) {
            window.clearInterval(interval);
          }*/
        }, 2500);
      }
    });
  });
	
	/* begin - Navigation Primary */
	var NavigationPrimary = {
	  init: function() {
			var c = this;
			var n = $('#menu-main-navigation');
	
			// Use bgiframe to fix dropdowns over selects if it's available.
			$.fn.bgiframe && $('li', n).bgiframe();
	
			// Mark parent elements so that we can style them with CSS
			$('> li', n).each(function() { c.markParents(this); });
	
	  	// Use the hoverintent plugin if it's available
	  	// if ($.fn.hoverIntent)
	  	//     {
	  	//   $('li', n).hoverIntent( {
	  	//     sensitivity: 1,
	  	//     over: this.mouseenter,
	  	//     out: this.mouseleave,
	  	//     timeout: 100
	  	//   });
	  	//     }
	  	// else
	  	  $('li', n).hover(this.mouseenter, this.mouseleave);
	  },
	  markParents: function(li) {
	    var c = this;
	    if ($('> ul', li).size() > 0)
		    $(li).addClass('parent').find('> a').addClass('parent').end().find('> ul li').each( function() { c.markParents(this); });
		},
		mouseenter: function() { $(this).addClass('over').children('a, span').addClass('over'); },
		mouseleave: function() { $(this).removeClass('over').children('a, span').removeClass('over'); }
	
	};
	$(function() { NavigationPrimary.init(); });
})(jQuery, window, document);



// jquery.ui.widget.min.js
/*! jQuery UI - v1.10.3 - 2013-05-03
* http://jqueryui.com
* Copyright 2013 jQuery Foundation and other contributors; Licensed MIT */
(function(e, t) {
    var i = 0, s = Array.prototype.slice, n = e.cleanData;
    e.cleanData = function(t) {
        for (var i, s = 0; null != (i = t[s]); s++)
            try {
                e(i).triggerHandler("remove")
        } catch (a) {}
        n(t)
    }, e.widget = function(i, s, n) {
        var a, r, o, h, l = {}, u = i.split(".")[0];
        i = i.split(".")[1], a = u + "-" + i, n || (n = s, s = e.Widget), e.expr[":"][a.toLowerCase()] = function(t) {
            return !!e.data(t, a)
        }, e[u] = e[u] || {}, r = e[u][i], o = e[u][i] = function(e, i) {
            return this._createWidget ? (arguments.length && this._createWidget(e, i), t) : new o(e, i)
        }, e.extend(o, r, {
            version: n.version,
            _proto: e.extend({}, n),
            _childConstructors: []
        }), h = new s, h.options = e.widget.extend({}, h.options), e.each(n, function(i, n) {
            return e.isFunction(n) ? (l[i] = function() {
                var e = function() {
                    return s.prototype[i].apply(this, arguments)
                }, t = function(e) {
                    return s.prototype[i].apply(this, e)
                };
                return function() {
                    var i, s = this._super, a = this._superApply;
                    return this._super = e, this._superApply = t, i = n.apply(this, arguments), this._super = s, this._superApply = a, i
                }
            }(), t) : (l[i] = n, t)
        }), o.prototype = e.widget.extend(h, {
            widgetEventPrefix: r ? h.widgetEventPrefix: i
        }, l, {
            constructor: o,
            namespace: u,
            widgetName: i,
            widgetFullName: a
        }), r ? (e.each(r._childConstructors, function(t, i) {
            var s = i.prototype;
            e.widget(s.namespace + "." + s.widgetName, o, i._proto)
        }), delete r._childConstructors) : s._childConstructors.push(o), e.widget.bridge(i, o)
    }, e.widget.extend = function(i) {
        for (var n, a, r = s.call(arguments, 1), o = 0, h = r.length; h > o; o++)
            for (n in r[o])
                a = r[o][n], r[o].hasOwnProperty(n) && a !== t && (i[n] = e.isPlainObject(a) ? e.isPlainObject(i[n]) ? e.widget.extend({}, i[n], a) : e.widget.extend({}, a) : a);
        return i
    }, e.widget.bridge = function(i, n) {
        var a = n.prototype.widgetFullName || i;
        e.fn[i] = function(r) {
            var o = "string" == typeof r, h = s.call(arguments, 1), l = this;
            return r=!o && h.length ? e.widget.extend.apply(null, [r].concat(h)) : r, o ? this.each(function() {
                var s, n = e.data(this, a);
                return n ? e.isFunction(n[r]) && "_" !== r.charAt(0) ? (s = n[r].apply(n, h), s !== n && s !== t ? (l = s && s.jquery ? l.pushStack(s.get()) : s, !1) : t) : e.error("no such method '" + r + "' for " + i + " widget instance") : e.error("cannot call methods on " + i + " prior to initialization; " + "attempted to call method '" + r + "'")
            }) : this.each(function() {
                var t = e.data(this, a);
                t ? t.option(r || {})._init() : e.data(this, a, new n(r, this))
            }), l
        }
    }, e.Widget = function() {}, e.Widget._childConstructors = [], e.Widget.prototype = {
        widgetName: "widget",
        widgetEventPrefix: "",
        defaultElement: "<div>",
        options: {
            disabled: !1,
            create: null
        },
        _createWidget: function(t, s) {
            s = e(s || this.defaultElement || this)[0], this.element = e(s), this.uuid = i++, this.eventNamespace = "." + this.widgetName + this.uuid, this.options = e.widget.extend({}, this.options, this._getCreateOptions(), t), this.bindings = e(), this.hoverable = e(), this.focusable = e(), s !== this && (e.data(s, this.widgetFullName, this), this._on(!0, this.element, {
                remove : function(e) {
                    e.target === s && this.destroy()
                }
            }),
            this.document = e(s.style ? s.ownerDocument: s.document || s),
            this.window = e(this.document[0].defaultView || this.document[0].parentWindow)),
            this._create(),
            this._trigger("create",
            null,
            this._getCreateEventData()),
            this._init()
        }, _getCreateOptions: e.noop, _getCreateEventData: e.noop, _create: e.noop, _init: e.noop, destroy: function() {
            this._destroy(), this.element.unbind(this.eventNamespace).removeData(this.widgetName).removeData(this.widgetFullName).removeData(e.camelCase(this.widgetFullName)), this.widget().unbind(this.eventNamespace).removeAttr("aria-disabled").removeClass(this.widgetFullName + "-disabled " + "ui-state-disabled"), this.bindings.unbind(this.eventNamespace), this.hoverable.removeClass("ui-state-hover"), this.focusable.removeClass("ui-state-focus")
        }, _destroy: e.noop, widget: function() {
            return this.element
        }, option: function(i, s) {
            var n, a, r, o = i;
            if (0 === arguments.length)
                return e.widget.extend({}, this.options);
            if ("string" == typeof i)
                if (o = {}, n = i.split(".")
                    , i = n.shift(), n.length) {
                for (a = o[i] = e.widget.extend({}, this.options[i]), r = 0; n.length-1 > r; r++)
                    a[n[r]] = a[n[r]] || {}, a = a[n[r]];
                if (i = n.pop(), s === t)
                    return a[i] === t ? null : a[i];
                a[i] = s
            } else {
                if (s === t)
                    return this.options[i] === t ? null : this.options[i];
                o[i] = s
            }
            return this._setOptions(o), this
        }, _setOptions: function(e) {
            var t;
            for (t in e)
                this._setOption(t, e[t]);
            return this
        }, _setOption: function(e, t) {
            return this.options[e] = t, "disabled" === e && (this.widget().toggleClass(this.widgetFullName + "-disabled ui-state-disabled", !!t).attr("aria-disabled", t), this.hoverable.removeClass("ui-state-hover"), this.focusable.removeClass("ui-state-focus")), this
        }, enable: function() {
            return this._setOption("disabled", !1)
        }, disable: function() {
            return this._setOption("disabled", !0)
        }, _on: function(i, s, n) {
            var a, r = this;
            "boolean" != typeof i && (n = s, s = i, i=!1), n ? (s = a = e(s), this.bindings = this.bindings.add(s)) : (n = s, s = this.element, a = this.widget()), e.each(n, function(n, o) {
                function h() {
                    return i || r.options.disabled!==!0&&!e(this).hasClass("ui-state-disabled") ? ("string" == typeof o ? r[o] : o).apply(r, arguments) : t
                }
                "string" != typeof o && (h.guid = o.guid = o.guid || h.guid || e.guid++);
                var l = n.match(/^(\w+)\s*(.*)$/), u = l[1] + r.eventNamespace, c = l[2];
                c ? a.delegate(c, u, h) : s.bind(u, h)
            })
        }, _off: function(e, t) {
            t = (t || "").split(" ").join(this.eventNamespace + " ") + this.eventNamespace, e.unbind(t).undelegate(t)
        }, _delay: function(e, t) {
            function i() {
                return ("string" == typeof e ? s[e] : e).apply(s, arguments)
            }
            var s = this;
            return setTimeout(i, t || 0)
        }, _hoverable: function(t) {
            this.hoverable = this.hoverable.add(t), this._on(t, {
                mouseenter: function(t) {
                    e(t.currentTarget).addClass("ui-state-hover")
                },
                mouseleave: function(t) {
                    e(t.currentTarget).removeClass("ui-state-hover")
                }
            })
        }, _focusable: function(t) {
            this.focusable = this.focusable.add(t), this._on(t, {
                focusin: function(t) {
                    e(t.currentTarget).addClass("ui-state-focus")
                },
                focusout: function(t) {
                    e(t.currentTarget).removeClass("ui-state-focus")
                }
            })
        }, _trigger: function(t, i, s) {
            var n, a, r = this.options[t];
            if (s = s || {}, i = e.Event(i)
                , i.type = (t === this.widgetEventPrefix ? t : this.widgetEventPrefix + t).toLowerCase(), i.target = this.element[0], a = i.originalEvent)for (n in a)
                n in i || (i[n] = a[n]);
            return this.element.trigger(i, s), !(e.isFunction(r) && r.apply(this.element[0], [i].concat(s))===!1 || i.isDefaultPrevented())
        }
    }, e.each({
        show : "fadeIn", hide : "fadeOut"
    }, function(t, i) {
        e.Widget.prototype["_" + t] = function(s, n, a) {
            "string" == typeof n && (n = {
                effect: n
            });
            var r, o = n ? n===!0 || "number" == typeof n ? i: n.effect || i: t;
            n = n || {}, "number" == typeof n && (n = {
                duration: n
            }), r=!e.isEmptyObject(n), n.complete = a, n.delay && s.delay(n.delay), r && e.effects && e.effects.effect[o] ? s[t](n) : o !== t && s[o] ? s[o](n.duration, n.easing, a) : s.queue(function(i) {
                e(this)[t](), a && a.call(s[0]), i()
            })
        }
    })
})(jQuery);


/*!
 * EventEmitter v4.2.0 - git.io/ee
 * Oliver Caldwell
 * MIT license
 * @preserve
 */

(function () {
    // Place the script in strict mode
    'use strict';

    /**
       * Class for managing events.
       * Can be extended to provide event functionality in other classes.
       *
       * @class EventEmitter Manages event registering and emitting.
       */
    function EventEmitter() {}

    // Shortcuts to improve speed and size

    // Easy access to the prototype
    var proto = EventEmitter.prototype;

    /**
       * Finds the index of the listener for the event in it's storage array.
       *
       * @param {Function[]} listeners Array of listeners to search through.
       * @param {Function} listener Method to look for.
       * @return {Number} Index of the specified listener, -1 if not found
       * @api private
       */
    function indexOfListener(listeners, listener) {
        var i = listeners.length;
        while (i--) {
            if (listeners[i].listener === listener) {
                return i;
            }
        }

        return -1;
    }

    /**
       * Returns the listener array for the specified event.
       * Will initialise the event object and listener arrays if required.
       * Will return an object if you use a regex search. The object contains keys for each matched event. So /ba[rz]/ might return an object containing bar and baz. But only if you have either defined them with defineEvent or added some listeners to them.
       * Each property in the object response is an array of listener functions.
       *
       * @param {String|RegExp} evt Name of the event to return the listeners from.
       * @return {Function[]|Object} All listener functions for the event.
       */
    proto.getListeners = function getListeners(evt) {
        var events = this._getEvents();
        var response;
        var key;

        // Return a concatenated array of all matching events if
        // the selector is a regular expression.
        if (typeof evt === 'object') {
            response = {};
            for (key in events) {
                if (events.hasOwnProperty(key) && evt.test(key)) {
                    response[key] = events[key];
                }
            }
        } else {
            response = events[evt] || (events[evt] = []);
        }

        return response;
    };

    /**
       * Takes a list of listener objects and flattens it into a list of listener functions.
       *
       * @param {Object[]} listeners Raw listener objects.
       * @return {Function[]} Just the listener functions.
       */
    proto.flattenListeners = function flattenListeners(listeners) {
        var flatListeners = [];
        var i;

        for (i = 0; i < listeners.length; i += 1) {
            flatListeners.push(listeners[i].listener);
        }

        return flatListeners;
    };

    /**
       * Fetches the requested listeners via getListeners but will always return the results inside an object. This is mainly for internal use but others may find it useful.
       *
       * @param {String|RegExp} evt Name of the event to return the listeners from.
       * @return {Object} All listener functions for an event in an object.
       */
    proto.getListenersAsObject = function getListenersAsObject(evt) {
        var listeners = this.getListeners(evt);
        var response;

        if (listeners instanceof Array) {
            response = {};
            response[evt] = listeners;
        }

        return response || listeners;
    };

    /**
       * Adds a listener function to the specified event.
       * The listener will not be added if it is a duplicate.
       * If the listener returns true then it will be removed after it is called.
       * If you pass a regular expression as the event name then the listener will be added to all events that match it.
       *
       * @param {String|RegExp} evt Name of the event to attach the listener to.
       * @param {Function} listener Method to be called when the event is emitted. If the function returns true then it will be removed after calling.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.addListener = function addListener(evt, listener) {
        var listeners = this.getListenersAsObject(evt);
        var listenerIsWrapped = typeof listener === 'object';
        var key;

        for (key in listeners) {
            if (listeners.hasOwnProperty(key) && indexOfListener(listeners[key], listener) === -1) {
                listeners[key].push(listenerIsWrapped ? listener : {
                    listener: listener,
                    once: false
                });
            }
        }

        return this;
    };

    /**
       * Alias of addListener
       */
    proto.on = proto.addListener;

    /**
       * Semi-alias of addListener. It will add a listener that will be
       * automatically removed after it's first execution.
       *
       * @param {String|RegExp} evt Name of the event to attach the listener to.
       * @param {Function} listener Method to be called when the event is emitted. If the function returns true then it will be removed after calling.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.addOnceListener = function addOnceListener(evt, listener) {
        return this.addListener(evt, {
            listener: listener,
            once: true
        });
    };

    /**
       * Alias of addOnceListener.
       */
    proto.once = proto.addOnceListener;

    /**
       * Defines an event name. This is required if you want to use a regex to add a listener to multiple events at once. If you don't do this then how do you expect it to know what event to add to? Should it just add to every possible match for a regex? No. That is scary and bad.
       * You need to tell it what event names should be matched by a regex.
       *
       * @param {String} evt Name of the event to create.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.defineEvent = function defineEvent(evt) {
        this.getListeners(evt);
        return this;
    };

    /**
       * Uses defineEvent to define multiple events.
       *
       * @param {String[]} evts An array of event names to define.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.defineEvents = function defineEvents(evts) {
        for (var i = 0; i < evts.length; i += 1) {
            this.defineEvent(evts[i]);
        }
        return this;
    };

    /**
       * Removes a listener function from the specified event.
       * When passed a regular expression as the event name, it will remove the listener from all events that match it.
       *
       * @param {String|RegExp} evt Name of the event to remove the listener from.
       * @param {Function} listener Method to remove from the event.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.removeListener = function removeListener(evt, listener) {
        var listeners = this.getListenersAsObject(evt);
        var index;
        var key;

        for (key in listeners) {
            if (listeners.hasOwnProperty(key)) {
                index = indexOfListener(listeners[key], listener);

                if (index !== -1) {
                    listeners[key].splice(index, 1);
                }
            }
        }

        return this;
    };

    /**
       * Alias of removeListener
       */
    proto.off = proto.removeListener;

    /**
       * Adds listeners in bulk using the manipulateListeners method.
       * If you pass an object as the second argument you can add to multiple events at once. The object should contain key value pairs of events and listeners or listener arrays. You can also pass it an event name and an array of listeners to be added.
       * You can also pass it a regular expression to add the array of listeners to all events that match it.
       * Yeah, this function does quite a bit. That's probably a bad thing.
       *
       * @param {String|Object|RegExp} evt An event name if you will pass an array of listeners next. An object if you wish to add to multiple events at once.
       * @param {Function[]} [listeners] An optional array of listener functions to add.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.addListeners = function addListeners(evt, listeners) {
        // Pass through to manipulateListeners
        return this.manipulateListeners(false, evt, listeners);
    };

    /**
       * Removes listeners in bulk using the manipulateListeners method.
       * If you pass an object as the second argument you can remove from multiple events at once. The object should contain key value pairs of events and listeners or listener arrays.
       * You can also pass it an event name and an array of listeners to be removed.
       * You can also pass it a regular expression to remove the listeners from all events that match it.
       *
       * @param {String|Object|RegExp} evt An event name if you will pass an array of listeners next. An object if you wish to remove from multiple events at once.
       * @param {Function[]} [listeners] An optional array of listener functions to remove.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.removeListeners = function removeListeners(evt, listeners) {
        // Pass through to manipulateListeners
        return this.manipulateListeners(true, evt, listeners);
    };

    /**
       * Edits listeners in bulk. The addListeners and removeListeners methods both use this to do their job. You should really use those instead, this is a little lower level.
       * The first argument will determine if the listeners are removed (true) or added (false).
       * If you pass an object as the second argument you can add/remove from multiple events at once. The object should contain key value pairs of events and listeners or listener arrays.
       * You can also pass it an event name and an array of listeners to be added/removed.
       * You can also pass it a regular expression to manipulate the listeners of all events that match it.
       *
       * @param {Boolean} remove True if you want to remove listeners, false if you want to add.
       * @param {String|Object|RegExp} evt An event name if you will pass an array of listeners next. An object if you wish to add/remove from multiple events at once.
       * @param {Function[]} [listeners] An optional array of listener functions to add/remove.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.manipulateListeners = function manipulateListeners(remove, evt, listeners) {
        var i;
        var value;
        var single = remove ? this.removeListener : this.addListener;
        var multiple = remove ? this.removeListeners : this.addListeners;

        // If evt is an object then pass each of it's properties to this method
        if (typeof evt === 'object' && !(evt instanceof RegExp)) {
            for (i in evt) {
                if (evt.hasOwnProperty(i) && (value = evt[i])) {
                    // Pass the single listener straight through to the singular method
                    if (typeof value === 'function') {
                        single.call(this, i, value);
                    } else {
                        // Otherwise pass back to the multiple function
                        multiple.call(this, i, value);
                    }
                }
            }
        } else {
            // So evt must be a string
            // And listeners must be an array of listeners
            // Loop over it and pass each one to the multiple method
            i = listeners.length;
            while (i--) {
                single.call(this, evt, listeners[i]);
            }
        }

        return this;
    };

    /**
       * Removes all listeners from a specified event.
       * If you do not specify an event then all listeners will be removed.
       * That means every event will be emptied.
       * You can also pass a regex to remove all events that match it.
       *
       * @param {String|RegExp} [evt] Optional name of the event to remove all listeners for. Will remove from every event if not passed.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.removeEvent = function removeEvent(evt) {
        var type = typeof evt;
        var events = this._getEvents();
        var key;

        // Remove different things depending on the state of evt
        if (type === 'string') {
            // Remove all listeners for the specified event
            delete events[evt];
        } else if (type === 'object') {
            // Remove all events matching the regex.
            for (key in events) {
                if (events.hasOwnProperty(key) && evt.test(key)) {
                    delete events[key];
                }
            }
        } else {
            // Remove all listeners in all events
            delete this._events;
        }

        return this;
    };

    /**
       * Emits an event of your choice.
       * When emitted, every listener attached to that event will be executed.
       * If you pass the optional argument array then those arguments will be passed to every listener upon execution.
       * Because it uses `apply`, your array of arguments will be passed as if you wrote them out separately.
       * So they will not arrive within the array on the other side, they will be separate.
       * You can also pass a regular expression to emit to all events that match it.
       *
       * @param {String|RegExp} evt Name of the event to emit and execute listeners for.
       * @param {Array} [args] Optional array of arguments to be passed to each listener.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.emitEvent = function emitEvent(evt, args) {
        var listeners = this.getListenersAsObject(evt);
        var listener;
        var i;
        var key;
        var response;

        for (key in listeners) {
            if (listeners.hasOwnProperty(key)) {
                i = listeners[key].length;

                while (i--) {
                    // If the listener returns true then it shall be removed from the event
                    // The function is executed either with a basic call or an apply if there is an args array
                    listener = listeners[key][i];
                    response = listener.listener.apply(this, args || []);
                    if (response === this._getOnceReturnValue() || listener.once === true) {
                        this.removeListener(evt, listeners[key][i].listener);
                    }
                }
            }
        }

        return this;
    };

    /**
       * Alias of emitEvent
       */
    proto.trigger = proto.emitEvent;

    /**
       * Subtly different from emitEvent in that it will pass its arguments on to the listeners, as opposed to taking a single array of arguments to pass on.
       * As with emitEvent, you can pass a regex in place of the event name to emit to all events that match it.
       *
       * @param {String|RegExp} evt Name of the event to emit and execute listeners for.
       * @param {...*} Optional additional arguments to be passed to each listener.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.emit = function emit(evt) {
        var args = Array.prototype.slice.call(arguments, 1);
        return this.emitEvent(evt, args);
    };

    /**
       * Sets the current value to check against when executing listeners. If a
       * listeners return value matches the one set here then it will be removed
       * after execution. This value defaults to true.
       *
       * @param {*} value The new value to check for when executing listeners.
       * @return {Object} Current instance of EventEmitter for chaining.
       */
    proto.setOnceReturnValue = function setOnceReturnValue(value) {
        this._onceReturnValue = value;
        return this;
    };

    /**
       * Fetches the current value to check against when executing listeners. If
       * the listeners return value matches this one then it should be removed
       * automatically. It will return true by default.
       *
       * @return {*|Boolean} The current value to check for or the default, true.
       * @api private
       */
    proto._getOnceReturnValue = function _getOnceReturnValue() {
        if (this.hasOwnProperty('_onceReturnValue')) {
            return this._onceReturnValue;
        } else {
            return true;
        }
    };

    /**
       * Fetches the events object and creates one if required.
       *
       * @return {Object} The events storage object.
       * @api private
       */
    proto._getEvents = function _getEvents() {
        return this._events || (this._events = {});
    };

    // Expose the class either via AMD, CommonJS or the global object
    if (typeof define === 'function' && define.amd) {
        define(function () {
            return EventEmitter;
        });
    } else if (typeof module !== 'undefined' && module.exports) {
        module.exports = EventEmitter;
    } else {
        this.EventEmitter = EventEmitter;
    }
}.call(this));
