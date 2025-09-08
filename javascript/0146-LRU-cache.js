/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.capacity = capacity
    this.cache = new Map()
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    const val = this.cache.get(key)
    if (typeof val == 'undefined') return -1

    this.cache.delete(key)
    this.cache.set(key, val)

    return val
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {

    this.cache.delete(key);
    if (this.cache.size == this.capacity) {
        this.cache.delete(this.cache.keys().next().value);
    }

    this.cache.set(key, value)
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */



// NON MAP IMPLEMENTATION (DOUBLE LINKED LIST)
/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.capacity = capacity
    this.nodeMap = {}
    this.size = 0

    this.startSentinal = new LinkedNode(null, null, null, null)
    this.endSentinal = new LinkedNode(null, null, null, this.startSentinal) 
    this.startSentinal.next = this.endSentinal
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    const node = this.nodeMap[key]
    if (!node) return -1

    node.next.prev = node.prev
    node.prev.next = node.next

    this.endSentinal.prev.next = node
    node.prev = this.endSentinal.prev

    this.endSentinal.prev = node
    node.next = this.endSentinal

    return node.value
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {

    const node = this.nodeMap[key];
    if (node) {
        node.prev.next = node.next
        node.next.prev = node.prev
        delete this.nodeMap[key]
        this.size -= 1
    }

    if (this.size == this.capacity) {
        const nodeToDelete = this.startSentinal.next
        nodeToDelete.next.prev = this.startSentinal
        this.startSentinal.next = nodeToDelete.next
        delete this.nodeMap[nodeToDelete.key]
        this.size -= 1
    }

    const newNode = new LinkedNode(key, value, this.endSentinal, this.endSentinal.prev)
    this.endSentinal.prev.next = newNode
    this.endSentinal.prev = newNode
    this.nodeMap[key] = newNode
    this.size += 1
};

var LinkedNode = function(key, value, next, prev) {
    this.next = next
    this.prev = prev
    this.key = key
    this.value = value
}

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
