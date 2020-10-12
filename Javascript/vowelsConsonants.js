

isVowel = (c) => {
    return "aeiou".indexOf(c) !== -1;
}

vowelsOrConsonants = (s) => {
    const toArray = s.split('');

    const vowels = toArray.filter(element => isVowel(element));
    const consonants = toArray.filter(element => !isVowel(element));

    const toPrint = vowels.concat(consonants);

    toPrint.map(element => console.log(element));
}

vowelsOrConsonants("javascriptloops");