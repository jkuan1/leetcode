/**
 * @param {number} n
 * @param {number} k
 * @param {number} target
 * @return {number}
 */
var numRollsToTarget = function(n, k, target) {
    const memoTable = Array.from({ length: n + 1 }, () => new Map());
    var memoize = function(diceIndex, currTarget) {
        if (diceIndex === 0) return currTarget === 0 ? 1 : 0;
        if (currTarget < 0) return 0;
        if (memoTable[diceIndex].has(currTarget)) return memoTable[diceIndex].get(currTarget)

        let ans = 0
        for (let i = 1; i <= k; i++) {
            ans = ( ans + memoize(diceIndex - 1, currTarget - i) ) % (1_000_000_007)
        } 
        memoTable[diceIndex].set(currTarget, ans)
        return ans
    }
    const ans = memoize(n, target)
    return ans
};


