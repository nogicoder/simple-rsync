*1) rsync core  should copy a file to a new place `rsync file1 new_name`

       expected: ""
            got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

       (compared using ==)

       Diff:
       @@ -1 +1,7 @@
       +Traceback (most recent call last):
       +  File "rsync.py", line 133, in <module>
       +    main()
       +  File "rsync.py", line 98, in main
       +    raise OSError("I haven't granted you the right!!")
       +OSError: I haven't granted you the right!!*

*2) rsync core  should copy a file to a new place `rsync file1 dir`

       expected: ""
            got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

       (compared using ==)

       Diff:
       @@ -1 +1,7 @@
       +Traceback (most recent call last):
       +  File "rsync.py", line 133, in <module>
       +    main()
       +  File "rsync.py", line 98, in main
       +    raise OSError("I haven't granted you the right!!")
       +OSError: I haven't granted you the right!!*

  *3) rsync core  should copy a file to a new place `rsync dir1/file1 dir2`

       expected: ""
            got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

       (compared using ==)

       Diff:
       @@ -1 +1,7 @@
       +Traceback (most recent call last):
       +  File "rsync.py", line 133, in <module>
       +    main()
       +  File "rsync.py", line 98, in main
       +    raise OSError("I haven't granted you the right!!")
       +OSError: I haven't granted you the right!!*

  *4) rsync core  should copy a file to a new place `rsync dir1/file1 dir2/new_name`

       expected: ""
            got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

       (compared using ==)

       Diff:
       @@ -1 +1,7 @@
       +Traceback (most recent call last):
       +  File "rsync.py", line 133, in <module>
       +    main()
       +  File "rsync.py", line 98, in main
       +    raise OSError("I haven't granted you the right!!")
       +OSError: I haven't granted you the right!!*

*5) rsync core  should work with the same file twice `rsync file1 file1`

       expected: ""
            got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

       (compared using ==)

       Diff:
       @@ -1 +1,7 @@
       +Traceback (most recent call last):
       +  File "rsync.py", line 133, in <module>
       +    main()
       +  File "rsync.py", line 98, in main
       +    raise OSError("I haven't granted you the right!!")
       +OSError: I haven't granted you the right!!*

  *6) rsync core  should work with the same file in different places `rsync file1 dir/file1`

       expected: ""
            got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

       (compared using ==)

       Diff:
       @@ -1 +1,7 @@
       +Traceback (most recent call last):
       +  File "rsync.py", line 133, in <module>
       +    main()
       +  File "rsync.py", line 98, in main
       +    raise OSError("I haven't granted you the right!!")
       +OSError: I haven't granted you the right!!*

  *7) rsync core  should work with the 2 different files `rsync file1 dir/file2`

       expected: ""
            got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

       (compared using ==)

       Diff:
       @@ -1 +1,7 @@
       +Traceback (most recent call last):
       +  File "rsync.py", line 133, in <module>
       +    main()
       +  File "rsync.py", line 98, in main
       +    raise OSError("I haven't granted you the right!!")
       +OSError: I haven't granted you the right!!*

*8) rsync core  should copy a link to a new place `rsync symlink new_name`

       expected: ""
            got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

       (compared using ==)

       Diff:
       @@ -1 +1,7 @@
       +Traceback (most recent call last):
       +  File "rsync.py", line 133, in <module>
       +    main()
       +  File "rsync.py", line 98, in main
       +    raise OSError("I haven't granted you the right!!")
       +OSError: I haven't granted you the right!!*

  *9) rsync core  should copy a link to a new place in a dir `rsync symlink dir`

       expected: ""
            got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

       (compared using ==)

       Diff:
       @@ -1 +1,7 @@
       +Traceback (most recent call last):
       +  File "rsync.py", line 133, in <module>
       +    main()
       +  File "rsync.py", line 98, in main
       +    raise OSError("I haven't granted you the right!!")
       +OSError: I haven't granted you the right!!*

  *10) rsync core  should copy a link to a new place `rsync hardlink new_name`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!*

  *11) rsync core  should copy a link to a new place in a dir `rsync hardlink dir`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!*

  *12) rsync core  should not change the content if the files have the same size and modtime `rsync file1 file2`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!*

  **13) rsync core  should change the content if the files have the same size and modtime `rsync -c file1 file2`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!**

  *14) rsync core  should change the content if the file is newer `rsync file1 file2`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!*

  **15) rsync core  should not change the content if the file is newer with -u `rsync -u file1 file2`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!**

*16) rsync core  should change the chmod for the 2 different files `rsync file1 dir/file2`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \..."rsync.py\", line 66, in check_update\n    if args.update:\nNameError: name 'args' is not defined\n"

        (compared using ==)

        Diff:
        @@ -1 +1,9 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 121, in main
        +    check_update(source_path, dest_path)  # CHANGE TO CHECKMODE
        +  File "rsync.py", line 66, in check_update
        +    if args.update:
        +NameError: name 'args' is not defined*

  *17) rsync core  should change the mtime for the 2 different files `rsync file1 dir/file2`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!*

  *18) rsync core  should create the new file with good mtime `rsync file1 new_name`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!*

  **19) rsync core  should not rewrite everything for a small change `rsync file1 dir/file2`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!**

  **20) rsync core  should not rewrite everything for a small change `rsync file1 dir/file2`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!**

  **21) rsync core  should not rewrite everything for a small change `rsync file1 dir/file2`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!**

  *22) rsync core  should generate an error if the src file doesn't exist `rsync file1 file2`

        expected: "rsync: link_stat "/app/rendu/wzrzvxnelnbfxiztyhh\" failed: No such file or directory (2)"
             got: "Traceback (most recent call last):"

        (compared using ==)*

*23) rsync core  should generate an error if the src file doesn't have the read right `rsync file1 file2`

        expected: "rsync: send_files failed to open \"/app/rendu/gzbaaonydfaqfqzkheu\": Permission denied (13)"
             got: "Traceback (most recent call last):"

        (compared using ==)*

*24) rsync core  should work as expected with -u everywhere `rsync -u -u -u -u file1 file2`

        expected: ""
             got: "Traceback (most recent call last):\n  File \"rsync.py\", line 133, in <module>\n    main()\n  File \... raise OSError(\"I haven't granted you the right!!\")\nOSError: I haven't granted you the right!!\n"

        (compared using ==)

        Diff:
        @@ -1 +1,7 @@
        +Traceback (most recent call last):
        +  File "rsync.py", line 133, in <module>
        +    main()
        +  File "rsync.py", line 98, in main
        +    raise OSError("I haven't granted you the right!!")
        +OSError: I haven't granted you the right!!*
