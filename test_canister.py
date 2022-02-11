from ic.canister import Canister
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent

iden = Identity()
client = Client()
agent = Agent(iden, client)


wicp_candid="""
type Metadata = record {
  fee : nat;
  decimals : nat8;
  owner : principal;
  logo : text;
  name : text;
  totalSupply : nat;
  symbol : text;
};
type Result = variant { Ok : nat; Err : TxError };
type TokenInfo = record {
  holderNumber : nat64;
  deployTime : nat64;
  metadata : Metadata;
  historySize : nat64;
  cycles : nat64;
  feeTo : principal;
};
type TxError = variant {
  InsufficientAllowance;
  InsufficientBalance;
  ErrorOperationStyle;
  Unauthorized;
  LedgerTrap;
  ErrorTo;
  Other;
  BlockUsed;
  AmountTooSmall;
};
service : (
  text,
  text,
  text,
  nat8,
  nat,
  principal,
  nat,
  principal,
  principal,
) -> {
  allowance : (principal, principal) -> (nat) query;
  approve : (principal, nat) -> (Result);
  balanceOf : (principal) -> (nat) query;
  decimals : () -> (nat8) query;
  getAllowanceSize : () -> (nat64) query;
  getBlockUsed : () -> (vec nat64) query;
  getHolders : (nat64, nat64) -> (vec record { principal; nat }) query;
  getMetadata : () -> (Metadata) query;
  getTokenInfo : () -> (TokenInfo) query;
  getUserApprovals : (principal) -> (vec record { principal; nat }) query;
  historySize : () -> (nat64) query;
  isBlockUsed : (nat64) -> (bool) query;
  logo : () -> (text) query;
  mint : (opt vec nat8, nat64) -> (Result);
  mintFor : (opt vec nat8, nat64, principal) -> (Result);
  name : () -> (text) query;
  owner : () -> (principal) query;
  setFee : (nat) -> ();
  setFeeTo : (principal) -> ();
  setGenesis : () -> (Result);
  setLogo : (text) -> ();
  setName : (text) -> ();
  setOwner : (principal) -> ();
  symbol : () -> (text) query;
  totalSupply : () -> (nat) query;
  transfer : (principal, nat) -> (Result);
  transferFrom : (principal, principal, nat) -> (Result);
  withdraw : (nat64, text) -> (Result);
}
"""
canister = Canister(agent=agent, canister_id="wjsrf-myaaa-aaaam-qaayq-cai", candid=wicp_candid)
res = canister.getTokenInfo()
print(res)
res = canister.totalSupply()
print(res)