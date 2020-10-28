from arxivscraper import Scraper
import pandas as pd
from pytz import timezone
from datetime import datetime, timedelta
from config import db


def arxiv_scraper():
    categories = ['cs', 'stat', 'econ', 'math', 'physics']

    for category in categories:
        print('Start scraping: {}'.format(category))
        scraper = Scraper(
            category=category.lower(),
            date_from=(datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
            date_until=datetime.now().strftime("%Y-%m-%d"),
            t=10
        )
        scraper_response = scraper.scrape()

        columns = ('id', 'title', 'categories', 'abstract', 'doi', 'created', 'updated', 'authors', 'affiliation')
        try:
            paper_data = pd.DataFrame(scraper_response, columns=columns)
            paper_data = paper_data.rename(
                columns={
                    'id': 'arxiv_id', 
                    'created': 'arxiv_created_at', 
                    'updated': 'arxiv_updated_at',
                    'categories': 'sub_categories'
                }
            )
            paper_data['category'] = category
            paper_data['is_emailed'] = 0
            paper_data['scraped_at'] = datetime.now()
            paper_data = paper_data.to_dict('records')

            stored_rsp = store_paper(paper_data)
            # print('Inserted responses: {}'.format(stored_rsp))
            print('Inserted!')
            return stored_rsp

        except Exception as ex:
            raise ex


def store_paper(paper_data):
    try:
        rsp = db.papers.insert_many(paper_data)

        return rsp.inserted_ids

    except Exception as ex:
        raise ex
