// Don't forget semi-colons. It probably won't throw errors but this isn't Python so follow the actual general convention.

const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

// Listens to an event 'tutorial' and triggers a functions.
eventEmitter.on('tutorial', () => { // This is equals to lambda: print('Tutorial event has occured...')
    console.log('Tutorial event has occured...');
});

// Emitted 'tutorial' event.
eventEmitter.emit('tutorial');


// Listens to an event 'tutorial-args' and triggers a functions.
eventEmitter.on('tutorial-args', (num1, num2) => { // This is equals to lambda num1, num2: print(num1 + num2)
    console.log(num1 + num2);
});

// Emitted 'tutorial-args' event with args.
eventEmitter.emit('tutorial-args', 1, 2);

// Class extending EventEmitter
class Person extends EventEmitter {
    constructor(name) {
        super();
        this._name = name
    }

    get name() {
        return this._name;
    }
}

// A new instance of the person...
// Note: Keyword 'let' character makes it a block scope (vs global or function). Might not matter here but keep it in mind for the future.
let pedro = new Person('Pedro');
let christina = new Person('Christina');

// Adding a listener on 'name' event for pedro/christina.
pedro.on('name', () => {
    console.log('my name is ' + pedro.name);
});

christina.on('name', () => {
    console.log('my name is ' + christina.name);
});


// Pedro emitting 'name' event. Events are emitted synchronously i.e. Pedro then Christina etc...
pedro.emit('name'); // Only triggers Pedro.
christina.emit('name'); // Only triggers Christina.
eventEmitter.emit('name'); // This is not part of Person class so this event won't trigger an anything.
