"""
itertools built-in module to create iterators
methods
itertools.count(start [,step]) # create a iterator starting from start,step default is 1
itertools.cycle(iterable)  # create a iterator from that iterable data
itertools.repeat(ele [,n]) # repeat ele n times if n is set or unlimited
itertools.acumulate(p [,func]) # returns an iterator producing running totals or accumulated results from other binary functions
itertools.chain(p,q,...) # combine multiple iterables (like lists, tuples, or strings) into a single, seamless iterator.
itertools.chain.from_iterable(iterable) #  flatten a single iterable containing multiple nested iterables. It serves as an alternate constructor for itertools.chain()
itertools.compress(data,selector) # It returns an iterator that yields elements from data only when the corresponding element in selectors evaluates to True. It stops as soon as either the data or the selectors iterable is exhausted
itertools.dropwhile(predicate, iterable) # creates an iterator that skips (drops) elements from the beginning of an iterable as long as a specified condition (the predicate) is true
itertools.filterfalse(predicate, iterable) # creates an iterator which filters elements from an iterable, returning only those for which the predicate function returns False
itertools.groupby(iterable,key=None) #  group consecutive elements of an iterable that share the same key
itertools.islice(iterable,start,stop [,step]) # returns an iterator that yields selected elements lazily, making it highly memory-efficient for large datasets or infinite streams. 
itertools.starmap(function,iterable) # apply a function to arguments that are already grouped in tuples or other iterables
itertools.takewhile(predicate, iterable) # returns an iterator yielding elements from an iterable as long as a specified condition (the predicate) remains True
itertools.tee(iterable,n=2) #Python Standard Library function that creates independent iterators from a single source. It is primarily used when you need to consume the same data stream multiple times without reconstructing the original iterator. 
itertools.zip_longest(*iterables,fillvalue=None) # aggregate elements from multiple iterables in parallel. Unlike the built-in zip() function, which stops when the shortest iterable is exhausted, zip_longest() continues until the longest iterable is finished.

"""
import itertools as itt


