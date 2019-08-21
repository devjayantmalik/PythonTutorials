# Create a program to convert markdown to html
# Supported Markdown tags are:
# Hashes: 1 - 6 : h1 - h6
# 3 dashes or 3 asterisk: hr
# ```language_name or ```code: pre <code>
# * or - or + to ul -> li
# 1. to N. : ol -> li
# *word* : italics
# **word** then: bold
# ~~word~~ tilde: strikethrough
# [text](url) : <a href="url">text</a>
# ![text](url) : <img src="url" alt="text"/>
# blank line: br

def get_start_html():
    # Write text to start of the html file
    return "<html><head></head><body>"

def get_end_html():
    # Write text to write at the end of the html file
    return "</body></html>"

def check_hashes(word):
    if word == "#":
        return "<h1>"

    elif word == "##":
        return "<h2>"

    elif word == "###":
        return "<h3>"

    elif word == "####":
        return "<h4>"

    elif word == "#####":
        return "<h5>"

    elif word == "######":
        return "<h6>"

    else:
        return False

def check_hr(word):
    if word == "---" or word == "***":
        return "<hr>"

    else:
        return False

def convert_source(line):
    # Create a variable to store the html
    html = ""
    end=""

    # Split each word in list
    words = line.split()

    # Cycle through each word and check
    for word in words:

        # Create a variable to store position of word
        pos = line.index(word)

        if word.isspace():
            html += " "

        # Check for hashes at start
        elif check_hashes(word) and pos == 0:
            # Get the equivalent html and add it to html
            eqHtml =  check_hashes(word)
            html += eqHtml + " "

            # Get the closing tag and add it to end
            end = eqHtml.replace('<', '</')

        # check for 3 dashes or asterisk
        elif check_hr(word) and pos == 0:
            # Get the equivalent html and add it to html
            eqHtml = check_hr(word)
            html += eqHtml + " "

            # Get the closing tag and add it to end
            end = "\n"
        else:
            html += word + " "



    # Return the html equivalent of the line
    return html + end


# Try to open a file and handle exception if file not found
try:
    source = open("/home/hp/temp/file1.md", mode="r", encoding="utf-8")
    dest = open("/home/hp/temp/file1.html", mode="w", encoding="utf-8")


except FileNotFoundError as ex:
    print("Invalid filename or filepath.")
    print(ex.args)

else:
    # Do something with file
    startText = get_start_html()
    dest.write(startText)

    # Read the file till the end
    while True:
        line = source.readline()
        if not line:

            break
        else:
            # Pass the line to convert_source function and
            # Write the received conversion to file.
            html = convert_source(line)
            dest.write(html)
            continue

    # Write the end text to html file
    endText = get_end_html()
    dest.write(endText)

    # Close the files
    source.close()
    dest.close()

finally:
    print("=" * 15)
    print("Thanks for using our software...")
    print("=" * 15)
