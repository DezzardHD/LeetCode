// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {        
        let mut res: Option<Box<ListNode>> = None;
        res = Self::compare(list1, list2);
        res
    }

    pub fn compare(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut new: Option<Box<ListNode>> = None;
        if let (Some(node1), Some(node2)) = (list1.as_ref(), list2.as_ref()) {
            if node1.val >= node2.val {
                return Some(Box::new(ListNode {
                    val: node2.val,
                    next: Self::compare(list1, node2.next.clone()),
                }));
            } else {
                return Some(Box::new(ListNode {
                    val: node1.val,
                    next: Self::compare(list2, node1.next.clone()),
                }));
            }
        }
        if list1.is_none() {
            if list2.is_some() {
                return list2.clone();
            }
        }
        if list2.is_none() {
            if list1.is_some() {
                return list1.clone();
            }
        }
        new

    }
}