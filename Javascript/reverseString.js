const reverseString = (s) => {
    let message = '';
    try{
        /*
            the method reverse only affects to arrays
            and thats why we need to first convert it into an array.
        */
        s = s.split('').reverse().join('');
    }
    catch (error){
        message = error.message;
    }
    finally {
        if (message !==  '')
            console.log(message);
        return s;
    }
}

console.log(reverseString("1234"));
console.log(reverseString(Number(1234)));