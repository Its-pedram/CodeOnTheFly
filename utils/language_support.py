ALLOWED_EXTENSIONS = {'py', 'cpp', 'java', 'js', 'ts', 'dart', 'go', 'php', 'c'}

compilers = {
    '.py': 'python3',
    '.cpp': 'g++',
    '.java': 'javac',
    '.js': 'node',
    '.ts': 'tsc',
    '.dart': 'dart',
    '.go': 'go',
    '.php': 'php',
    '.c': 'gcc',
}

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