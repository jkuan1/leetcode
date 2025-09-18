// More comprehensive heap solution to practice heaps

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {

    if (nums.length == k) return nums

    const map = new Map()
    for(let i = 0; i < nums.length; i++) {
        const value = nums[i]
        const occurances = map.get(value) || 0
        map.set(value, occurances + 1 )
    }
    const values = map.keys()
    const heap = new CustomMaxHeap()
    for (const value of values) {
        const node = new Node(value, map.get(value))
        heap.insert(node)
    }
    
    return heap.extractMaxValues(k)

};

class CustomMaxHeap {
    constructor(){
        this.arr = []
    }
    left(i){
        return i * 2 + 1
    }
    right(i){
        return i * 2 + 2
    }
    parent(i){
        return Math.floor((i - 1) / 2)
    }
    insert(node){
        let arr = this.arr
        arr.push(node)

        let i = arr.length - 1
        while (i > 0 && arr[this.parent(i)].occurances < arr[i].occurances) {
            let p = this.parent(i);
            [arr[i], arr[p]] = [arr[p], arr[i]]
            i = p
        }
    }
    extractMax(){
        if (this.arr.length === 0) return null
        if (this.arr.length === 1) return this.arr.pop()

        let max = this.arr[0]
        this.arr[0] = this.arr.pop()
        this.heapifyMax(0)
        return max
    }
    heapifyMax(i){
        let arr = this.arr
        if (arr.length === 1) return
        let left = this.left(i)
        let right = this.right(i)

        let largestIndex = i

        if (left < arr.length && arr[left].occurances > arr[largestIndex].occurances) largestIndex = left;
        if (right < arr.length && arr[right].occurances > arr[largestIndex].occurances) largestIndex = right;
        
        if (largestIndex != i) {
            [arr[i], arr[largestIndex]] = [arr[largestIndex], arr[i]]
            this.heapifyMax(largestIndex)
        }
    }
    extractMaxValues(k){
        const ans = []
        while (ans.length < k) {
            const max = this.extractMax()
            ans.push(max.value)
        }
        return ans
    }
}

class Node {
    constructor(value, occurances) {
        this.value = value
        this.occurances = occurances
    }
}
