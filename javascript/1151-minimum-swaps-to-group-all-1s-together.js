/**
 * @param {number[]} data
 * @return {number}
 */
var minSwaps = function(data) {
    const numOnes = data.filter(x => x == 1).length

    let startIndex = 0
    let endIndex = numOnes - 1

    let currOnesInSubArray = data.slice(startIndex, endIndex + 1).filter(x => x == 1).length
    let maxOnesInSubArray = currOnesInSubArray

    startIndex += 1
    endIndex += 1

    while (endIndex < data.length) {
        if (data[startIndex - 1] == 0 && data[endIndex] == 1) {
            currOnesInSubArray += 1
            maxOnesInSubArray = maxOnesInSubArray < currOnesInSubArray ? currOnesInSubArray : maxOnesInSubArray
        }
        if (data[startIndex - 1] == 1 && data[endIndex] == 0) {
            currOnesInSubArray -= 1
        }
        startIndex += 1
        endIndex += 1
    }

    return numOnes - maxOnesInSubArray
};
