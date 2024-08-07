from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:  %(message)s')

project_name = 'StudentPerformance'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/component/__init__.py',
    f'src/{project_name}/component/data_ingestion.py',
    f'src/{project_name}/component/data_transformation.py',
    f'src/{project_name}/component/model_trainer.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/pipeline/train_pipeline.py',
    f'src/{project_name}/pipeline/predict_pipeline.py',
    f'src/{project_name}/exception.py',
    f'src/{project_name}/logger.py',
    f'src/{project_name}/utils.py',
    'src/templates/index.html',
    'requirements.txt',
    'setup.py',
    'app.py'
]

# Create directories and files for the project structure
for filepath in list_of_files:
    path = Path(filepath)

    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f'Created directory {path.parent} for {path.name}')

    if not path.exists() or path.stat().st_size == 0:
        path.touch()
        logging.info(f'Created empty file {path}')
    else:
        logging.info(f'{path.name} already exists')
