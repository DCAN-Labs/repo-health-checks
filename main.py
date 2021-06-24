import csv


def main():
    git_lab_projects = set()
    with open('/home/miran045/reine097/projects/repo-health-checks/data/repo_health_checks_GitLab.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                git_lab_projects.add(row[0])
                line_count += 1
        print(f'Processed {line_count} lines.')
    git_hub_projects = set()
    with open('/home/miran045/reine097/projects/repo-health-checks/data/repo_health_checks_GitHub.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                git_hub_projects.add(row[0])
                line_count += 1
        print(f'Processed {line_count} lines.')

        common = git_lab_projects.intersection(git_hub_projects)
        print(common)

if __name__ == '__main__':
    main()
