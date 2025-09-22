/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kthFactor = function(n, k) {

    if (k == 1) return 1
    k -= 1

    const scanLimit = Math.sqrt(n)
    const factors = [1]

    for (let i = 2; i <= scanLimit; i ++) {
        if (n % i == 0) {
            k -= 1
            if ( k == 0) return i
            if (i * i == n) break
            factors.push(i)
        }
    }

    for (let i = factors.length - 1; i >= 0; i --) {
        const newFactor = n / factors[i]
        k -= 1
        if  (k == 0) return newFactor
    }

    return -1
};

