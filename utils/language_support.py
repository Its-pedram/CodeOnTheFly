# Add acceptable file extensions here. Users can only upload files with one of the extensions below.
ALLOWED_EXTENSIONS = {'py', 'cpp', 'java', 'js', 'ts', 'dart', 'go', 'c'}

# This dictionary decides which file extension corresponds to which compiler/interpreter. 
compilers = {
    '.py': 'python3',
    '.cpp': 'g++',
    '.java': 'javac',
    '.js': 'node',
    '.ts': 'tsc',
    '.dart': 'dart',
    '.go': 'go',
    '.c': 'gcc',
}

# This is where you define the command syntax for each compiler/interpreter.
def generate_compiler_command(filename, compiler):
    if compiler == 'python3':
        return filename
    elif compiler == 'g++':
        return f" -o {filename.rsplit('.', 1)[0]}.out {filename}"
    elif compiler == 'javac':
        return f" -d {filename.rsplit('.', 1)[0]}.class {filename}"
    elif compiler == 'node':
        return f" {filename}"
    elif compiler == 'tsc':
        return f" {filename}"
    elif compiler == 'dart':
        return f" {filename}"
    elif compiler == 'go':
        return f" {filename}"
    elif compiler == 'gcc':
        return f" -o {filename.rsplit('.', 1)[0]}.out {filename}"