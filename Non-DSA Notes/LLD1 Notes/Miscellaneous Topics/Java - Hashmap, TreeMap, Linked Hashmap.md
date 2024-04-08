## Java Collections - Hashmap, Linked Hashmap & Tree Map

- Hashmap
- Linked Hashmap 
- TreeMap


A **hash map** is good as a general-purpose map implementation that provides rapid storage and retrieval operations. However, it falls short because of its chaotic and unorderly arrangement of entries.

A **linked hash map** possesses the good attributes of hash maps and adds order to the entries. It performs better where there is a lot of iteration because only the number of entries is taken into account regardless of capacity.

A **tree map** takes ordering to the next level by providing complete control over how the keys should be sorted. On the flip side, it offers worse general performance than the other two alternatives.

### 1. Hashmap
Let’s first look at what it means that HashMap is a map. A map is a key-value mapping, which means that every key is mapped to exactly one value and that we can use the key to retrieve the corresponding value from a map.

The advantage of a HashMap is that the time complexity to insert and retrieve a value is O(1) on average. We have covered the internal workings in the video lectures already. 
Before we proceed Let’s summarize how the put and get operations work.

**Put()**
When we add an element to the map, HashMap calculates the bucket. If the bucket already contains a value, the value is added to the list (or tree) belonging to that bucket. If the load factor becomes bigger than the maximum load factor of the map, the capacity is doubled.

**Get()**
When we want to get a value from the map, HashMap calculates the bucket and gets the value with the same key from the list (or tree).

**Example Code**
Lets try to create a hashmap of products. We will create a Product class first.
```java
public class Product {

    private String name;
    private String description;
    private List<String> tags;
    
    // standard getters/setters/constructors

    public Product addTagsOfOtherProduct(Product product) {
        this.tags.addAll(product.getTags());
        return this;
    }
}
```
We can now create a HashMap with the key of type String and elements of type Product:

```java
Map<String, Product> productsByName = new HashMap<>();
```
**1. Put Method**
Adding to hashmap.
```java
Product eBike = new Product("E-Bike", "A bike with a battery");
Product roadBike = new Product("Road bike", "A bike for competition");
//using the Put Method
productsByName.put(eBike.getName(), eBike);
productsByName.put(roadBike.getName(), roadBike);
```

**2. Get Method**
We can retrieve a value from the map by its key:
```java
Product nextPurchase = productsByName.get("E-Bike");
assertEquals("A bike with a battery", nextPurchase.getDescription());
```

If we try to find a value for a key that doesn’t exist in the map, we’ll get a null value:

**3. Remove**

We can remove a key-value mapping from the HashMap:
```java
productsByName.remove("E-Bike");
assertNull(productsByName.get("E-Bike"));
```

**4. Contains Key**
To check if a key is present in the map, we can use the containsKey() method:
```java
productsByName.containsKey("E-Bike");
```

-----
**Hashmap with Custom Key Class**
We can use any class as the key in our HashMap. However, for the map to work properly, we need to provide an implementation for equals() and hashCode(). 
In most cases, we should use **immutable keys**. Or at least, we must be aware of the consequences of using mutable keys. If key changes after insertion, HashMap will be searching in the wrong bucket and leading to inconsistent behaviour.


Let’s say we want to have a map with the product as the key and the price as the value:

```java
HashMap<Product, Integer> priceByProduct = new HashMap<>();
priceByProduct.put(eBike, 900);
```
Let’s implement the equals() and hashCode() methods:


```java
//Override these methods in the Product Class
@Override
public boolean equals(Object o) {
    if (this == o) {
        return true;
    }
    if (o == null || getClass() != o.getClass()) {
        return false;
    }

    Product product = (Product) o;
    return Objects.equals(name, product.name) &&
      Objects.equals(description, product.description);
}

@Override
public int hashCode() {
    return Objects.hash(name, description);
}
```
Note that `hashCode()` and `equals()` need to be overridden only for classes that we want to use as map keys, not for classes that are only used as values in a map.

-----

### 2. Linked Hashmap 
The LinkedHashMap class is very similar to HashMap in most aspects. However, the linked hash map is based on both hash table and linked list to enhance the functionality of hash map.

It maintains a doubly-linked list running through all its entries in addition to an underlying array of default size 16.

This linked list defines the order of iteration, which by default is the order of insertion of elements (insertion-order).

Let’s have a look at a linked hash map instance which orders its entries according to how they’re inserted into the map. It also guarantees that this order will be maintained throughout the life cycle of the map:

```java
public void givenLinkedHashMap_whenGetsOrderedKeyset_thenCorrect() {
    LinkedHashMap<Integer, String> map = new LinkedHashMap<>();
    map.put(1, null);
    map.put(2, null);
    map.put(3, null);
    map.put(4, null);
    map.put(5, null);

    Set<Integer> keys = map.keySet();
    Integer[] arr = keys.toArray(new Integer[0]);

    for (int i = 0; i < arr.length; i++) {
        assertEquals(new Integer(i + 1), arr[i]);
    }
}
```
We can guarantee that this test will always pass as the insertion order will always be maintained. We cannot make the same guarantee for a HashMap.

**Access Order Linked Hashmap**
LinkedHashMap provides a special constructor which enables us to specify, among custom load factor (LF) and initial capacity, a different ordering mechanism/strategy called access-order:
```java
LinkedHashMap<Integer, String> map = new LinkedHashMap<>(16, .75f, true);
```
The first parameter is the initial capacity, followed by the load factor and the last param is the ordering mode. So, by passing in true, we turned on access-order, whereas the default was insertion-order.

This mechanism ensures that the order of iteration of elements is the order in which the elements were last accessed, from least-recently accessed to most-recently accessed.

**LRU using LinkedHashmap**
And so, building a Least Recently Used (LRU) cache is quite easy and practical with this kind of map. A successful put or get operation results in an access for the entry:
```java
public void givenLinkedHashMap_whenAccessOrderWorks_thenCorrect() {
    LinkedHashMap<Integer, String> map 
      = new LinkedHashMap<>(16, .75f, true);
    map.put(1, null);
    map.put(2, null);
    map.put(3, null);
    map.put(4, null);
    map.put(5, null);

    Set<Integer> keys = map.keySet();
    assertEquals("[1, 2, 3, 4, 5]", keys.toString());
 
    map.get(4);
    assertEquals("[1, 2, 3, 5, 4]", keys.toString());
 
    map.get(1);
    assertEquals("[2, 3, 5, 4, 1]", keys.toString());
 
    map.get(3);
    assertEquals("[2, 5, 4, 1, 3]", keys.toString());
}

```
Just like HashMap, LinkedHashMap implementation is not synchronized. So if you are going to access it from multiple threads and at least one of these threads is likely to change it structurally, then it must be externally synchronized.
```java
Map m = Collections.synchronizedMap(new LinkedHashMap());
```
We will learn more about concurrency in a separate tutorial.

-----
### 3. TreeMap ###
TreeMap is a map implementation that keeps its entries sorted according to the natural ordering of its keys or better still using a comparator if provided by the user at construction time.

By default, TreeMap sorts all its entries according to their natural ordering. For an integer, this would mean ascending order and for strings, alphabetical order.A hash map does not guarantee the order of keys stored and specifically does not guarantee that this order will remain the same over time, but a tree map guarantees that the keys will always be sorted according to the specified order.


TreeMap, unlike a hash map and linked hash map, does not employ the hashing principle anywhere since it does not use an array to store its entries but uses a self-balanancing tree such as **Red Black Tree** data structure to store the entries.
A red-black tree is a self-balancing binary search tree. This attribute and the above guarantee that basic operations like search, get, put and remove take logarithmic time O(log n) as For every insertion and deletion, the maximum height of the tree on any edge is maintained at O(log n) i.e. the tree balances itself continuously.

Just like hash map and linked hash map, a tree map is not synchronized and therefore the rules for using it in a multi-threaded environment are similar to those in the other two map implementations.


A Tree Map example with Comparator
```java
public void givenTreeMap_whenOrdersEntriesByComparator_thenCorrect() {
    TreeMap<Integer, String> map = 
      new TreeMap<>(Comparator.reverseOrder());
    map.put(3, "val");
    map.put(2, "val");
    map.put(1, "val");
    map.put(5, "val");
    map.put(4, "val");
        
    assertEquals("[5, 4, 3, 2, 1]", map.keySet().toString());
}
```
Notice that we placed the integer keys in a non-orderly manner but on retrieving the key set, we confirm that they are indeed maintained in ascending order. This is the natural ordering of integers.

We now know that TreeMap stores all its entries in sorted order. Because of this attribute of tree maps, we can perform queries like; find “largest”, find “smallest”, find all keys less than or greater than a certain value, etc.
```java
public void givenTreeMap_whenPerformsQueries_thenCorrect() {
    TreeMap<Integer, String> map = new TreeMap<>();
    map.put(3, "val");
    map.put(2, "val");
    map.put(1, "val");
    map.put(5, "val");
    map.put(4, "val");
        
    Integer highestKey = map.lastKey();
    Integer lowestKey = map.firstKey();
    Set<Integer> keysLessThan3 = map.headMap(3).keySet();
    Set<Integer> keysGreaterThanEqTo3 = map.tailMap(3).keySet();

    assertEquals(new Integer(5), highestKey);
    assertEquals(new Integer(1), lowestKey);
    assertEquals("[1, 2]", keysLessThan3.toString());
    assertEquals("[3, 4, 5]", keysGreaterThanEqTo3.toString());
}
```









