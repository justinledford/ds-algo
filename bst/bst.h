#ifndef BST_H
#define BST_H

struct bst_node {
    struct bst_node *left;
    struct bst_node *right;
    int key;
};


struct bst {
    struct bst_node *root;
};


struct bst *bst_init();
struct bst_node *_bst_init_node(int key);

void _bst_insert(struct bst_node* root, int key);
void bst_insert(struct bst* tree, int key);

int _bst_contains(struct bst_node *root, int key);
int bst_contains(struct bst *tree, int key);

struct bst_node** _bst_scsr(struct bst_node** node);
void _bst_delete(struct bst_node **node);

struct bst_node **_bst_find(struct bst_node **node, int key);
void bst_delete(struct bst *tree, int key);

void _bst_print(struct bst_node* root);
void bst_print(struct bst *tree);

void bst_free(struct bst *tree);
void _bst_free(struct bst_node *root);

#endif
