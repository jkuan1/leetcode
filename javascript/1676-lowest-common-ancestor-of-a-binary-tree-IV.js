/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode[]} nodes
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, nodes) {
    let set = new Set(nodes.map(n => n.val))
    
    function dfs(root){
        if(!root) return
        if(set.has(root.val)) return root
        
        let left = dfs(root.left)
        let right = dfs(root.right)
        if(left && right) return root
        return left ? left : right
    }
    return dfs(root)
};
