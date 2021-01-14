import yaml
import sys
import click

sys.path.append('../../../paulovn/python-aiml')
import aiml


# This is a script to automate testing of the AIML interpreter
# Takes a YAML containing testing scenarii and runs them

yaml_file = open("test_scenarii/wildcards.yaml", 'r')
yaml_content = yaml.load(yaml_file)

#print(yaml_content)
for test in yaml_content:
    k = aiml.Kernel()
    k.verbose(False)
    click.secho(test['test'], bold=True)
    k.learn(test['file'])
    for step in test['steps']:
        click.echo('\t Input: ' + step['input'])
        response = k.respond(step['input'])
        if response == step['expected output']:
            click.secho('\t[SUCCESS] Response: "' + response +'"', fg='green')
        else :
            click.secho('\t[FAIL] Response: "' + response +'"\t Expected: "' + step['expected output'] + '"', fg='red')
    click.echo('\n-----------------------------------------------------------\n')
