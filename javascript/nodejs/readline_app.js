// Don't forget semi-colons. It probably won't throw errors but this isn't Python so follow the actual general convention.
const readline = require('readline');

/* Creating an interface...
Passing in an Object (JSON?), with two properties.
The 'process' is a global object i.e. provided by node hence we don't need to require it.

1. input  : process.stdin
2. output : process.stdout 
*/
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

// Creating a sample problem for readline interface demo.
let num1 = Math.floor((Math.random() * 10) + 1); // This is generating a random number between 1 and 10.
let num2 = Math.floor((Math.random() * 10) + 1); // This is generating a random number between 1 and 10.
let answ = num1 + num2;

// The string in `` (backticks) is probably equals to f-string in Python but needs $ sign before {} curly-brackets.
rl.question(`What is ${num1} + ${num2}? \n`, (userInput) => {
    if (userInput.trim() == answ) {
        rl.close(); // Emits 'close' event.
    }
    else {
        rl.setPrompt('Incorrect response... Please try again. \n'); // Sets a prompt.
        rl.prompt(); // Calls a prompt.
        /*
        This is an event loop. 
        The 'line' event is emitted whenever the input stream receives an end-of-line input (\n, \r, or \r\n). 
        This usually occurs when the user presses the <Enter>, or <Return> keys.
        */
        rl.on('line', (userInput) => { 
            if (userInput.trim() == answ) {
                rl.close();
            }
            else {
                rl.setPrompt(`Your answer of ${userInput} is incorrect... Please try again. \n`)
                rl.prompt()
            }
        })
    }
});

// Listening on close event.
rl.on('close', () => {
    console.log('Correct!!')
});
