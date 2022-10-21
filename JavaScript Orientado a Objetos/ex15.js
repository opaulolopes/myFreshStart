var arr1 = [3, 'a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9, 3]
var occurence = {};
var comparison = 0;
var mostFrequent;

(function (array) {
    for (c = 0, array.length; c < array.length; c++) {
        let element = array[c];

        if (occurence[element] === undefined) {
            occurence[element] = 1;
        } else {
            occurence[element] = occurence[element] + 1;
        }
        if (occurence[element] > comparison) {
            comparison = occurence[element];
            mostFrequent = array[c];
        }
    }
    console.log(`${mostFrequent}: ${comparison} vezes`)
})(arr1)