#include <stdlib.h>
#include <stdio.h>
#include "bst.h"

struct bst *bst_init()
{
    struct bst *tree;
    tree = malloc(sizeof(struct bst));
    *tree = (struct bst){.root = NULL};
    return tree;
}


struct bst_node *_bst_init_node(int key)
{
    struct bst_node *node;
    node = malloc(sizeof(struct bst_node));
    *node = (struct bst_node){.left = NULL, .right = NULL, .key = key};
    return node;
}


void _bst_insert(struct bst_node* root, int key)
{
    struct bst_node **p;

    if (root == NULL) return;
    p = (key < root->key) ? &root->left : &root->right;

    if (*p)
        _bst_insert(*p, key);
    else
        *p = _bst_init_node(key);
}


void bst_insert(struct bst* tree, int key)
{
    if (tree->root)
        _bst_insert(tree->root, key);
    else
        tree->root = _bst_init_node(key);
}


int _bst_contains(struct bst_node *root, int key)
{
    struct bst_node **p;

    if (root == NULL) return 0;
    if (key == root->key) return 1;

    p = (key < root->key) ? &root->left : &root->right;
    return _bst_contains(*p, key);
}


int bst_contains(struct bst *tree, int key)
{
    return _bst_contains(tree->root, key);
}


struct bst_node** _bst_scsr(struct bst_node** node)
{
    while ((*node)->left != NULL)
        node = &(*node)->left;
    return node;
}


void _bst_delete(struct bst_node **node)
{
    struct bst_node *tmp, *child, **scsr;

    if (!(*node)) return;

    /* Case 1: No children
     * Just delete
     */
    if ((*node)->left == NULL && (*node)->right == NULL) {
        tmp = *node;
        *node = NULL;
        free(tmp);
        return;
    }

    /* Case 2: One child
     * Replace node with child
     */
    if (!(*node)->left != !(*node)->right) {
        child = (!!(*node)->left) ? (*node)->left : (*node)->right;
        tmp = *node;
        *node = child;
        free(tmp);
        return;
    }

    /* Case 3: Two children
     * Replace values in node with in-order successor,
     * then delete successor
     */
    if ((*node)->left && (*node)->right) {
        scsr = _bst_scsr(&(*node)->right);
        (*node)->key = (*scsr)->key;
        return _bst_delete(scsr);
    }
}


struct bst_node **_bst_find(struct bst_node **node, int key)
{
    struct bst_node **p;

    if (*node == NULL) return NULL;
    if (key == (*node)->key) return node;

    p = (key < (*node)->key) ? &(*node)->left : &(*node)->right;
    return _bst_find(p, key);
}


void bst_delete(struct bst *tree, int key)
{
    struct bst_node **node;

    node = _bst_find(&tree->root, key);
    if (node)
        _bst_delete(node);
}


void _bst_print(struct bst_node* root)
{
    if (!root) return;
    if (root->left) _bst_print(root->left);
    printf("%d, ", root->key);
    if (root->right) _bst_print(root->right);
}


void bst_print(struct bst *tree)
{
    if (tree->root)
        _bst_print(tree->root);
}


void _bst_free(struct bst_node *root)
{
    if (!root) return;

    if (!root->left && !root->right)
        free(root);

    _bst_free(root->left);
    _bst_free(root->right);
}


void bst_free(struct bst *tree)
{
    _bst_free(tree->root);
    free(tree);
}
