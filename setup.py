from setuptools import setup, find_packages
    
    with open('README.md', encoding='utf-8') as f: # README.md 내용 읽어오기
        long_description = f.read()
    
    setup(
        name                = 'tootorch',
        version             = '0.1', # PyPI에 올릴 version 
        long_description    = long_description, # README.md 내용을 PyPI project Description에 넣기
        long_description_content_type = 'text/markdown', # 형식은 markdown으로 지정
        description         = 'Implemetation XAI in Computer Vision (Pytorch)', # 짦은 소개
        author              = 'Jaehuck Heo', # 이름
        author_email        = 'wogur379@gmail.com', # 메일 
        url                 = 'https://github.com/TooTouch/tootorch', # github url
        download_url        = 'https://github.com/TooTouch/tootorch/archive/v0.1.tar.gz', # release 이름
        install_requires    =  ["torch","torchvision","h5py","tqdm","pillow","opencv-python"], # 패키지 사용시 필요한 모듈
        packages            = find_packages(exclude = []),
        keywords            = ['tootorch','XAI'], # 키워드
        python_requires     = '>=3.6', # python 필요 버전
        package_data        = {}, 
        zip_safe            = False,
        classifiers         = [   
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
