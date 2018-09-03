"""
class of Huobi restful api client
"""
from huobi.rest.endpoints.common import HuobiRestClientCommon
from huobi.rest.endpoints.market import HuobiRestClientMarket
from huobi.rest.endpoints.account import HuobiRestClientAccounts
from huobi.rest.endpoints.order import HuobiRestClientOrder


class HuobiRestClient(
    HuobiRestClientMarket,
    HuobiRestClientCommon,
    HuobiRestClientAccounts,
    HuobiRestClientOrder,
):
    """
    Huobi restful api client
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.store_accounts:
            self._store_accounts()

    def _store_accounts(self):
        """Store working account id for each type"""
        working_accounts = {}
        accounts = self.accounts().data['data']
        for account in accounts:
            if account['state'] == 'working':
                working_accounts[account['type']] = account['id']
        self.spot_account_id = working_accounts.get('spot')
        self.margin_account_id = working_accounts.get('margin')
        self.otc_account_id = working_accounts.get('otc')
