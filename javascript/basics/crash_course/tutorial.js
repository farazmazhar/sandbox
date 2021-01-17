const sum = (num1, num2) => num1 + num2;
const sub = (num1, num2) => num1 - num2;
const PI = 3.14;

class SomeMathObject {
    constructor() {
        console.log('Object created...')
    }
}

// module.exports.sum = sum;
// module.exports.sub = sub;
// module.exports.PI = PI;
// module.exports.SomeMathObject = SomeMathObject;

module.exports = {
    sum: sum,
    sub: sub,
    PI: PI,
    SomeMathObject: SomeMathObject
}
