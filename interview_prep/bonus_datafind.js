function dataFinder(data) {
    return function find(valueToFind, minRange = 0, maxRange = data.length - 1) {
        let foundIndex = -1;

        for (let i = minRange; i <= maxRange; i++) {
            if (data[i] === valueToFind) {
                foundIndex = i;
                break; // Exit the loop once found
            }
        }

        return foundIndex !== -1 ?
            { found: true, index: foundIndex } :
            { found: false, error: 'value out of range' };
    }
}