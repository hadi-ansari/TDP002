#! /usr/bin/env python3

def quick_sort(l, func):
   if len(l) <= 1:
      return l
   
   pivot = l[-1]
   l2 = l.copy()
   for i in range(len(l2) - 1):
      if func(l2[i]) >= func(pivot):
         item = l2[i]
         l.remove(item)
         l.append(item)

   gt_pivot = l[l.index(pivot) + 1: ]
   lt_pivot = l[0:l.index(pivot)]
      
   sorted_left = quick_sort(lt_pivot, func)
   sorted_right = quick_sort(gt_pivot, func)

   sorted_list = sorted_left
   sorted_list.append(pivot)
   sorted_list.extend(sorted_right)

   return sorted_list
      
    
def main():
   
    l1 = [100,2,5,6,1,9,7,8]
    l2 = [11, 4]
    print("{}\n{}\n{}\nl1 = {}\n".format("Exempel1","="*30, "Osorterad lista:",l1))

    print("{}\n{}\n{}".format("Sorterad lista:", "print(quick_sort(l1, lambda x: x))", quick_sort(l1, lambda x: x)))
    print()
    db = [('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')]
    print("{}\n{}\n{}\ndb = {}\n".format("Exempel2","="*30, "Osorterad lista:",db))

    print("{}\n{}\n{}".format("Sorterad lista:", "print(quick_sort(db, lambda e: e[0]))", quick_sort(db, lambda e: e[0])))
    

# ------------------------------ huvudprogram ------------------------------
if __name__ == "__main__":
    main()
