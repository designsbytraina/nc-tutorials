from sqlalchemy.orm import sessionmaker
from models import Deals, db_connect, create_deals_table


class LivingSocialPipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""

    def __init__(self):
        """Initializes database connection and sessionmaker.

        Creates deals table.

        """

        engine = db_connect()
        create_deals_table(engine)
        # Create session
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """

        session = self.Session()
        # Unpack deals item
        deal = Deals(**item)

        try:
            # Add deal to session
            session.add(deal)
            # Commit changes to db
            session.commit()
            
        except:
            session.rollback()
            raise

        finally:
            # Close session
            session.close()

        return item
