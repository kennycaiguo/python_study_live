def warnings_demo1():
    import warnings
    
    warnings.simplefilter("always")
    
    def fxn():
        warnings.warn("this is a warning", Warning)
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fxn()
    
    with warnings.catch_warnings(category=Warning):
        warnings.warn("this is a warning2", Warning)
    
    warnings.warn("this is a warning3", Warning)
    
    def fxn2():
        warnings.warn("deprecated", DeprecationWarning)
    
    with warnings.catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        # Trigger a warning.
        fxn2()
        # Verify some things
        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert "deprecated" in str(w[-1].message)

def warnings_demo2():
    # warnings模块说明
    import warnings
    
    a,b= 1,23
    class Twarnings(Warning):
        pass
    try:
        assert a == 2
    except Exception as e:
        warnings.warn('wrong!',Twarnings)

if __name__  == '__main__':
    # warnings_demo1()        
    warnings_demo2()        